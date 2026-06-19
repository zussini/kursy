Zmiany v2:

1. 4_3 SVM liniowy:
   - dodano dokładne rozróżnienie: f(x), margines funkcyjny y*f(x), margines geometryczny y*f(x)/||w||,
   - dodano tabelę z obliczaniem marginesów w przykładzie 1D,
   - rozbudowano sekcję soft margin i parametr C,
   - dodano tabelę punkt-po-punkcie: f(x), y*f(x), odległość od granicy, xi, status punktu, support vector.

2. 4_4 SVM kernelowy:
   - rozbudowano wyjaśnienie kernel trick,
   - dodano macierze kernela: linear, polynomial degree 2, RBF,
   - dodano tabelę porównującą kernele linear/poly/RBF/sigmoid,
   - doprecyzowano wpływ gamma i relację C + gamma,
   - zamieniono ciężki interaktywny slider gamma na lżejsze statyczne wykresy.

3. 4_5 SVM w praktyce:
   - rozbudowano opis praktycznego workflow: Pipeline, skalowanie, train/test, GridSearchCV,
   - dodano diagnostykę support vectors,
   - dodano opcjonalny trudniejszy wariant binarny: cyfry 3 vs 8.

4. 4_1 i 4_2:
   - uporządkowano język i numerację,
   - usunięto niepotrzebne helpery grafowe,
   - w QDA doprecyzowano, skąd bierze się granica kwadratowa.

Wszystkie notebooki zostały wykonane po zmianach i zapisane z aktualnymi outputami.
