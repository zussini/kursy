"""Gotowa symulacja i sprawdzanie odpowiedzi do ćwiczenia."""

import argparse
import csv
from dataclasses import dataclass
from math import cos, log, sin, sqrt, tau
from pathlib import Path


LICZBA_RAMION = 10
LICZBA_PROB = 1000
EPSILONY = (0.0, 0.01, 0.1)
ODCHYLENIA = {"A": (1.0,), "B": (0.2, 2.0)}
OKNA = ((1, 50), (901, 1000))
MASKA = 0xFFFFFFFF


def mieszaj32(x):
    """Wspólny dla JavaScript i Pythona sposób tworzenia ziaren."""
    x ^= x >> 16
    x = (x * 0x7FEB352D) & MASKA
    x ^= x >> 15
    x = (x * 0x846CA68B) & MASKA
    return x ^ (x >> 16)


class Strumien:
    """Prosty generator zgodny z symulacją w przeglądarce."""

    def __init__(self, ziarno, swiat, identyfikator):
        self.stan = mieszaj32(ziarno ^ mieszaj32(swiat + 1) ^ identyfikator) or 0x6D2B79F5
        self.w_rezerwie = None

    def jednostajna(self):
        x = self.stan
        x ^= (x << 13) & MASKA
        x ^= x >> 17
        x ^= (x << 5) & MASKA
        self.stan = x
        return (x + 0.5) / 4294967296

    def normalna(self):
        if self.w_rezerwie is not None:
            gotowa, self.w_rezerwie = self.w_rezerwie, None
            return gotowa
        # Transformacja Boxa–Mullera daje dwie liczby z N(0, 1).
        promien = sqrt(-2 * log(self.jednostajna()))
        kat = tau * self.jednostajna()
        self.w_rezerwie = promien * sin(kat)
        return promien * cos(kat)


@dataclass
class Agent:
    sigma: float
    epsilon: float
    oceny: list
    liczniki: list
    nagrody: list
    trafienia: list


def symuluj(tryb, swiaty, ziarno, wybierz_ramie, aktualizuj_ocene):
    """Zwróć wyniki dwóch ustalonych okien dla każdej strategii."""
    scenariusze = [(sigma, epsilon) for sigma in ODCHYLENIA[tryb] for epsilon in EPSILONY]
    wyniki = [([0.0, 0.0], [0, 0]) for _ in scenariusze]
    for swiat in range(swiaty):
        los_srednich = Strumien(ziarno, swiat, 0xA511E9B3)
        los_szumu = Strumien(ziarno, swiat, 0x63D83595)
        los_akcji = Strumien(ziarno, swiat, 0x9E3779B9)
        q = [los_srednich.normalna() for _ in range(LICZBA_RAMION)]
        najlepsza_srednia = max(q)

        agenci = [
            Agent(sigma, epsilon, [0.0] * LICZBA_RAMION, [0] * LICZBA_RAMION, nagrody, trafienia)
            for (sigma, epsilon), (nagrody, trafienia) in zip(scenariusze, wyniki)
        ]
        for t in range(1, LICZBA_PROB + 1):
            # Te same losowania dla wszystkich strategii i wariantów sigma.
            szum = [los_szumu.normalna() for _ in range(LICZBA_RAMION)]
            u, v = los_akcji.jednostajna(), los_akcji.jednostajna()
            okno = None
            if t <= OKNA[0][1]:
                okno = 0
            elif t >= OKNA[1][0]:
                okno = 1
            for agent in agenci:
                a = wybierz_ramie(agent.oceny, agent.epsilon, u, v)
                R = q[a] + agent.sigma * szum[a]
                aktualizuj_ocene(agent.oceny, agent.liczniki, a, R)
                if okno is not None:
                    agent.nagrody[okno] += R
                    agent.trafienia[okno] += q[a] == najlepsza_srednia

    tabela = []
    for (sigma, epsilon), (nagrody, trafienia) in zip(scenariusze, wyniki):
        for i, (od, do) in enumerate(OKNA):
            n = swiaty * (do - od + 1)
            tabela.append(
                {
                    "proba_od": od,
                    "proba_do": do,
                    "swiaty": swiaty,
                    "ziarno": ziarno,
                    "sigma": sigma,
                    "epsilon": epsilon,
                    "srednia_wyplata": nagrody[i] / n,
                    "najlepsze_ramie_proc": 100 * trafienia[i] / n,
                }
            )
    return tabela


def sprawdz(wybierz_ramie, aktualizuj_ocene):
    """Sprawdź obie funkcje na małych przykładach."""
    def sprawdz_wybor():
        assert wybierz_ramie([2.0, -1.0, 0.0], 0, 0.4, 0.9) == 0, "Greedy wybiera najwyższe Q."
        assert wybierz_ramie([2.0, -1.0, 0.0], 0.1, 0.03, 0.9) == 2, "Przy u < ε losujemy spośród wszystkich ramion."
        assert wybierz_ramie([0.0, 2.0, 2.0], 0, 0.4, 0.2) == 1, "Przy remisie może wypaść pierwszy lider."
        assert wybierz_ramie([0.0, 2.0, 2.0], 0, 0.4, 0.8) == 2, "Przy remisie może wypaść drugi lider."

    def sprawdz_srednia():
        Q = [0.0, 0.0]
        N = [0, 0]
        for R, srednia in zip((2, -1, 5), (2.0, 0.5, 2.0)):
            aktualizuj_ocene(Q, N, 1, R)
            assert Q[1] == srednia, f"Po wypłacie {R} średnia powinna wynosić {srednia}."
        assert N == [0, 3], "Licznik rośnie tylko dla wybranego ramienia."
        assert Q[0] == 0.0, "Ocena drugiego ramienia się nie zmienia."

    sukces = True
    for nazwa, proba in (
        ("wybierz_ramie", sprawdz_wybor),
        ("aktualizuj_ocene", sprawdz_srednia),
    ):
        try:
            proba()
        except NotImplementedError:
            print(f"Uzupełnij funkcję {nazwa}.")
            sukces = False
        except AssertionError as blad:
            print(f"Sprawdź funkcję {nazwa}. {blad}")
            sukces = False
        else:
            print(f"Funkcja {nazwa} działa w sprawdzanych przykładach.")
    return sukces


def uruchom(wybierz_ramie, aktualizuj_ocene):
    parser = argparse.ArgumentParser(description="Eksploracyjne laboratorium bandytów.")
    parser.add_argument("tryb", choices=("sprawdz", "A", "B"), help="Sprawdź kod lub uruchom doświadczenie A albo B.")
    parser.add_argument("--swiaty", type=int, default=200, help="Liczba światów. Domyślnie 200.")
    parser.add_argument("--ziarno", type=int, default=7, help="Ziarno losowania. Domyślnie 7.")
    parser.add_argument("--csv", type=Path, metavar="PLIK", help="Zapisz tabelę pod wskazaną nazwą.")
    opcje = parser.parse_args()
    if opcje.tryb == "sprawdz":
        raise SystemExit(0 if sprawdz(wybierz_ramie, aktualizuj_ocene) else 1)
    if opcje.swiaty < 1:
        parser.error("Liczba światów musi być dodatnia.")
    if not 0 <= opcje.ziarno <= MASKA:
        parser.error("Ziarno musi być od 0 do 4294967295.")
    try:
        tabela = symuluj(opcje.tryb, opcje.swiaty, opcje.ziarno, wybierz_ramie, aktualizuj_ocene)
    except NotImplementedError:
        parser.exit(1, "Najpierw uzupełnij funkcje i uruchom tryb sprawdz.\n")

    print(f"Doświadczenie {opcje.tryb} · {opcje.swiaty} światów × {LICZBA_PROB} prób · ziarno {opcje.ziarno}")
    print(f"{'σ':>4}  {'ε':>4}  {'Próby':>9}  {'Śr. wypłata':>11}  {'Najlepsze ramię':>15}")
    for wiersz in tabela:
        proby = f'{wiersz["proba_od"]}–{wiersz["proba_do"]}'
        sigma = f'{wiersz["sigma"]:.1f}'.replace(".", ",")
        epsilon = f'{wiersz["epsilon"]:.2f}'.replace(".", ",")
        srednia = f'{wiersz["srednia_wyplata"]:.3f}'.replace(".", ",")
        udzial = f'{wiersz["najlepsze_ramie_proc"]:.1f}%'.replace(".", ",")
        print(f"{sigma:>4}  {epsilon:>4}  {proby:>9}  {srednia:>11}  {udzial:>15}")

    if opcje.csv is not None:
        with opcje.csv.open("w", encoding="utf-8-sig", newline="") as plik:
            zapis = csv.DictWriter(plik, list(tabela[0]))
            zapis.writeheader()
            zapis.writerows(tabela)
        print(f"Tabela zapisana w {opcje.csv}.")
