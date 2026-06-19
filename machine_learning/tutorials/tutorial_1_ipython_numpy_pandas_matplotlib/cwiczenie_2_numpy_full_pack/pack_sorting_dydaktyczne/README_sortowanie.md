# Pakiet: sortowanie algorytmiczne (dydaktyczne)

Pliki:
- `cwiczenie_2_numpy_sortowanie_algorytmy_core.py`
- `cwiczenie_2_numpy_sortowanie_algorytmy_student_exercises.ipynb`
- `cwiczenie_2_numpy_sortowanie_algorytmy_student_exercises_done.ipynb`

Założenie dydaktyczne:
- notebook nie konkuruje z `sorted()` ani `np.sort`,
- celem jest zrozumienie:
  - stabilności,
  - in-place vs out-of-place,
  - roli rekurencji,
  - różnicy między `O(n^2)` i `O(n log n)`,
  - tego, dlaczego insertion sort pomaga na prawie posortowanych danych,
  - tego, dlaczego merge sort i quicksort skalują się lepiej.

Proponowane użycie na zajęciach:
1. Omówić sekcję 0-1 bardzo wolno, z przejściem po małych przykładach.
2. Dać studentom do samodzielnej implementacji:
   - bubble sort,
   - selection sort,
   - insertion sort.
3. Potem przejść do rekurencji:
   - `merge`,
   - `merge_sort`,
   - `partition_lomuto`,
   - `quicksort_inplace`.
4. Na końcu uruchomić benchmark i wspólnie omówić:
   - dlaczego insertion sort dobrze wypada na danych prawie posortowanych,
   - dlaczego naiwny quicksort może tracić na danych odwróconych,
   - dlaczego w praktyce i tak używamy `sorted()` / `list.sort()` / `np.sort`.
