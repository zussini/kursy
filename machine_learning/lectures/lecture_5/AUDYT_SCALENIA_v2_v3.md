# Audyt scalenia v2/v3 — decyzje plik po pliku

| Plik | Decyzja |
|---|---|
| `0_0_mapa_kursu_i_kolejnosc_metod.ipynb` | v3 było lepsze od v2, ale przepisałem mapę tak, żeby jasno ustawić kolejność i rolę `0_1`. |
| `0_1_odleglosci_macierze_sasiedztwa_knn_fundament_recznie.ipynb` | scalone: struktura dydaktyczna z v2 + poprawiona notacja z v3 + nowe panele $\varepsilon$ i $k$. |
| `1_1_umap_interaktywny.ipynb` | zachowane z v3; to już był dobry panel Plotly. |
| `1_2_tsne_interaktywny_macierz_dopasowania.ipynb` | zachowane z v3; to już był dobry panel Plotly z macierzami $P$, $Q$ i błędem. |
| `1_3_pca_kontrast_liniowy.ipynb` | zachowane + dodany panel obracania osi projekcji. |
| `2_1_pca_recznie_matematycznie.ipynb` | zachowane; ujednolicono Markdown/LaTeX. |
| `2_2_tsne_recznie_pelny_algorytm.ipynb` | zachowane; ujednolicono Markdown/LaTeX. |
| `2_3_umap_recznie_pelny_algorytm.ipynb` | zachowane; ujednolicono Markdown/LaTeX. |
| `2_4_umap_tsne_similarity_scores_recznie.ipynb` | zachowane; ujednolicono Markdown/LaTeX. |
| `3_1_knn_recznie_graf_i_klasyfikacja.ipynb` | zachowane; dobrze pasuje po `0_1`. |
| `3_2_dbscan_recznie_eps_core_border_noise.ipynb` | zachowane + dodany panel $\varepsilon$ dla core/border/noise. |
| `3_3_kmeans_recznie_centroidy_i_sse.ipynb` | wybrana wersja v3, bo ma lepszy elbow plot; poprawiono LaTeX i dodano suwak iteracji. |
| `3_4_porownanie_knn_dbscan_kmeans.ipynb` | wybrana wersja v3, bo lepiej porównuje metody na jednym zbiorze; dodano panel KNN dla różnych $k$. |
| `4_1_lda_recznie_supervised_pca.ipynb` | wybrana wersja v3, bo lepiej pokazuje projekcję 2D → 1D; poprawiono LaTeX i dodano panel kierunku projekcji. |
| `4_2_qda_recznie_gaussy_i_granice_kwadratowe.ipynb` | zachowane; ujednolicono Markdown/LaTeX. |
| `4_3_svc_svm_recznie_margines_soft_margin.ipynb` | wybrana wersja SVC/soft-margin; poprawiono LaTeX, zapis HTML i wyświetlanie `fig.show()`. |
| `4_4_svm_kernel_xor_intuicja.ipynb` | zachowane; ujednolicono Markdown/LaTeX. |

## Dlaczego nie zostawiłem duplikatów `0_1_v2` i `0_1_v3_latex`?

Bo dydaktycznie robiły szum. W głównej ścieżce powinien być jeden canonical notebook `0_1`. Wersja v4 zawiera najlepsze elementy obu.
