# Notebooki v3: confusion matrices + porównanie z drzewami

Zmiany względem v2:

- Dodano macierze pomyłek tam, gdzie model zwraca klasy: LDA, QDA, SVC liniowy i SVC kernelowy.
- Doprecyzowano, że `supervised` oznacza uczenie z etykietami, a macierz pomyłek ma sens dla klasyfikacji, nie dla regresji.
- W notebooku praktycznym `4_5` dodano normalizowaną macierz pomyłek oraz listę najczęstszych pomyłek.
- Dodano porównanie SVM z `DecisionTreeClassifier` i `RandomForestClassifier` na tym samym zbiorze `digits`.
- W `4_4` dodano krótki kontrast: kernel SVM rozwiązuje XOR przez podobieństwa/margines, drzewo przez osiowe reguły decyzyjne.
