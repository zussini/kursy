## Ćwiczenie: “czytanie stanu” CartPole na żywo (bez uczenia)

W CartPole obserwacja to wektor:

\[
s=(x,\dot x,\theta,\dot\theta)
\]

- \(x\): położenie wózka (lewo/prawo)
- \(\dot x\): prędkość wózka
- \(\theta\): kąt kija względem pionu (0 = pion)
- \(\dot\theta\): prędkość kątowa (jak szybko kij “ucieka”)

### Jak interpretować sytuację?
Kluczowa jest para \((\theta,\dot\theta)\):

- jeśli \(\theta\cdot \dot\theta > 0\) ⇒ kij **ucieka dalej** (pogarsza się)
- jeśli \(\theta\cdot \dot\theta < 0\) ⇒ kij **wraca / hamuje przechył** (lepiej)

### Zadanie
1. Uruchom kod poniżej.
2. Obserwuj wydruki co 10 kroków.
3. Zwróć uwagę na sytuacje, gdy \(\theta>0\) i \(\dot\theta>0\) (oraz analogicznie dla ujemnych).
## Pytania (odpowiedz krótko)

1) Co się dzieje z epizodem, gdy \(|\theta|\) zaczyna rosnąć i \(\theta\cdot\dot\theta>0\)?

2) Jeśli w pewnym momencie widzisz:
- \(\theta>0\) i \(\dot\theta>0\)

to **jaka akcja** (0=lewo, 1=prawo) wydaje Ci się intuicyjnie sensowna, żeby “podjechać pod kij” — i dlaczego?

3) Analogicznie: co byś zrobił dla \(\theta<0\) i \(\dot\theta<0\)?

