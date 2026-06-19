Wersja v3: dodano macierze pomyłek oraz porównanie SVM z drzewami decyzyjnymi.

Zmiany główne:
- 4_1: LDA jako projekcja + prosty próg klasyfikacyjny + confusion matrix.
- 4_2: train/test dla LDA i QDA + confusion matrices.
- 4_3: confusion matrices dla różnych C oraz wyjaśnienie, że macierz pomyłek nie zastępuje analizy marginesu/slack.
- 4_4: confusion matrices dla linear/poly/RBF na XOR + krótki most SVM vs drzewa.
- 4_5: dokładniejsze confusion matrices, wersja procentowa oraz porównanie SVC RBF z DecisionTree, DecisionTree max_depth=8 i RandomForest.

Uwaga techniczna:
- Interaktywne suwaki Plotly w 4_1 i 4_3 są zapisywane do HTML. Inline fig.show() jest zakomentowane, aby notebook łatwiej wykonywał się wsadowo. W Jupyter można odkomentować fig.show(), jeśli chcemy widzieć suwak bezpośrednio pod komórką.
