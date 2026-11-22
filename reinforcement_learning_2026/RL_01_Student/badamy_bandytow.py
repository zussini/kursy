"""Uzupełnij dwa TODO. Zastąp raise NotImplementedError własnym kodem.

Po zapisaniu obu funkcji uruchom: python badamy_bandytow.py sprawdz
"""

from laboratorium import uruchom


def wybierz_ramie(Q, epsilon, u, v):
    """Zwróć indeks ramienia według reguły ε-zachłannej.

    Q[a] to bieżąca ocena ramienia o indeksie a. Indeksy zaczynają się od 0.
    epsilon to prawdopodobieństwo eksploracji. Symulator podaje liczby
    u i v z przedziału [0, 1).
    """
    # Przed kodem: dla Q = [2, 5, 5, 0], epsilon = 0.10 i u = 0.40
    # pula to [1, 2]. Przy v = 0.75 wybór pada na pozycję 1, czyli ramię 2.
    # Przewidź, co się zmieni przy u = 0.05 i tym samym v.
    #
    # TODO 1. Przełóż na Python pseudokod wyboru:
    # 1. Jeśli u < epsilon, do puli wpisz wszystkie indeksy ramion.
    # 2. W przeciwnym razie wpisz do puli indeksy ramion z najwyższą oceną Q.
    # 3. Zachowaj rosnącą kolejność indeksów. Pomnóż v przez długość puli
    #    i weź część całkowitą jako pozycję. Zwróć indeks ramienia z tej pozycji.
    raise NotImplementedError


def aktualizuj_ocene(Q, N, a, nagroda):
    """Zaktualizuj na miejscu listy Q i N po wypłacie z ramienia a."""
    # Przed kodem: jeśli wybrane ramię ma N[a] = 1 i Q[a] = -1,
    # to po nagrodzie +3 licznik wynosi 2, a średnia wynosi 1.
    #
    # TODO 2. Przełóż na Python pseudokod aktualizacji średniej:
    # 1. Zwiększ licznik wyborów ramienia a o jeden.
    # 2. Odejmij dotychczasową ocenę ramienia a od nowej nagrody.
    # 3. Podziel różnicę przez nowy licznik i dodaj wynik do oceny ramienia a.
    raise NotImplementedError


if __name__ == "__main__":
    uruchom(wybierz_ramie, aktualizuj_ocene)
