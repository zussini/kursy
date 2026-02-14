# Wstęp/Introduction

# Kursy AI – repozytorium edukacyjne

To repozytorium docelowo będzie zawierać różne kursy, w pierwszej kolejności związane z szeroko pojętą sztuczną inteligencją (AI). Kolejne moduły i materiały będą dodawane sukcesywnie.

Celem jest stworzenie kursów, które:

- są dostępne dla osób na różnych poziomach zaawansowania,
- prowadzą od intuicji i podstaw do bardziej zaawansowanych koncepcji,
- pozwalają rzeczywiście zrozumieć mechanizmy działania algorytmów,
- zawierają ćwiczenia wspierające samodzielne myślenie i praktykę.

---

## Przykładowe ścieżki

### Deep Learning (DL)

W kursie DL przechodzimy m.in. przez:

- zrozumienie działania filtrów w sieciach konwolucyjnych (CNN),
- budowę i trening sieci konwolucyjnej,
- analizę cech wyższych warstw i ich interpretację.

### Reinforcement Learning (RL)

W kursie RL pojawiają się m.in.:

- implementacja klasycznych środowisk (np. GridWorld w duchu Sutton & Barto),
- własne implementacje algorytmów,
- przejście od metod tablicowych do aproksymacji funkcji i metod głębokich.

---

## Autorskie elementy/implementacje

W repozytorium znajdują się również autorskie implementacje i pomysły dydaktyczne, m.in.:

- implementacja „Odkurzacza” (układu dwustanowego),
- ręcznie wykonana sieć neuronowa wraz z propagacją wsteczną (backpropagation), w pełni przeliczone w arkuszu kalkulacyjnym inspirowane książką Josha Starmera,
- ścieżka dydaktyczna/struktura kursu, dużo elementów przejść między tematami jest zaprojektowane w sposób ciągły, aby powstała jedna spójna historia.

Wiele z tych implementacji powstało z potrzeby wyjaśnienia konkretnych zagadnień w sposób maksymalnie przejrzysty — takich materiałów nie mogłe znaleźć albo były porozrzucane między różnymi repozytoriami w otwartym dostępie (lub były dostępne wyłącznie komercyjnie).

---

## Filozofia dydaktyczna

Każdy temat będzie opatrzony ćwiczeniami, które pomagają:

- zbudować intuicję,
- przejść od teorii do praktyki,
- samodzielnie przeanalizować problem,
- zachowanie ciągłości loginczej między tematami, starałem się łączyć kolejne notebooki między sobą, są nawet przedstawione zależności dalekozasięgowe jak połączenie implementacji wczesnych z DL z późnymi w RL - głębokim uczeniem ze wzmocnieniem.

Jednocześnie celem nie jest tworzenie „czarnej magii bez rozwiązań”. Staram się zachować pewną równowagę pomiędzy:

- podaniem wiedzy i materiałów (rozwiązanych lub częściowo rozwiązanych)
- a pozostawieniem przestrzeni na samodzielne przetworzenie materiału poprzez zadania.

Metoda pracy wciąż ewoluuje i krystalizuje się wraz z rozwojem kursów — szczególnie widoczne jest to w najnowszych częściach RL i DL.

---

Repozytorium:  
👉 https://github.com/zussini/kursy

Docelowo chciałbym, aby to repozytorium było również po angielsku, ale w pierwszej kolejności 
chcę je utrzymywać w języku polskim. Dopiero, potem, będę tłumaczył, prawdodpobnie automatycznie
z lekkimi korektami, jeśli znajdą się błędy.
 
# Licensing Model (Dual License)

This repository uses a content-type-based dual license.

## 1. Code — MIT License

All executable source code is licensed under the MIT License.

This includes:

* Python, Julia, or other source files
* Scripts and utilities
* Model implementations
* Training loops
* Experimental pipelines
* Code cells inside Jupyter notebooks

You may use this code commercially.

See `LICENSE`.

---

## 2. Educational Content — CC BY-NC-SA 4.0

All instructional and explanatory materials are licensed under
Creative Commons Attribution-NonCommercial-ShareAlike 4.0.

This includes:

* Markdown cells inside notebooks
* Written explanations
* Mathematical derivations
* Exercise descriptions
* Course structure and pedagogical sequencing
* Diagrams and figures

You may not use this material for commercial purposes.

See `LICENSE-CONTENT`.

---

If a file contains both code and instructional text (e.g., Jupyter notebooks),
the executable code portions are licensed under MIT, while the instructional
and explanatory text is licensed under CC BY-NC-SA 4.0.

© 2026 Piotr Kuterba

