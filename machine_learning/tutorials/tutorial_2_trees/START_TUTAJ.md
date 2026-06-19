# START_TUTAJ

Otwieraj notebooki w tej kolejności:

```text
1. cwiczenia_wyklad_4_01_reczne_gini_drzewo_student_doprecyzowane.ipynb
2. cwiczenia_wyklad_4_02_progi_liczbowe_drzewo_regresyjne_student_doprecyzowane.ipynb
3. cwiczenia_wyklad_4_03_random_forest_churn_student_podniesione.ipynb
4. cwiczenia_wyklad_4_04_gradient_boosting_xgboost_churn_student_boosting_zamkniete_lr_iteracje.ipynb
5. cwiczenia_wyklad_4_05_auto_xgboost_podsumowanie_student_neutral_appendix.ipynb
```

Wersje `rozwiazania` zawierają gotowe obliczenia i komentarze. Wersje `executed` są kontrolne — mają już wyniki wykonania.

## Co jest celem kolejnych notebooków?

```text
4.1  policzyć Gini i zbudować pierwsze drzewo ręcznie
4.2  zrozumieć progi liczbowe i różnicę klasyfikacja/regresja
4.3  zobaczyć, co Random Forest dodaje do pojedynczego drzewa
4.4  zobaczyć, jak boosting buduje sekwencję poprawek
4.5  zastosować całą wiedzę w szybkim porównaniu modeli
```

## Najważniejsze dopowiedzenie do 4.4

W 4.4 nie wybieramy jednego najlepszego drzewa. Końcowy model to suma:

```text
F0 + eta*T1 + eta*T2 + eta*T3 + ...
```

Dlatego w tym notebooku szczególnie ważne są sekcje pokazujące:

- kolejne stump-y,
- predykcję nowego klienta,
- wpływ `learning_rate`,
- wpływ liczby iteracji.
