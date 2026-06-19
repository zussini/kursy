# Rozszerzenie projektu o dane społeczno-ekonomiczne

## Zalecana jednostka analizy

Najłatwiej łączyć dane na poziomie gminy lub powiatu, najlepiej przez identyfikatory TERYT. Łączenie samych nazw może prowadzić do niejednoznaczności.

## Proponowane zmienne

- ludność i gęstość zaludnienia,
- saldo migracji i udział osób 65+,
- dochody własne i wydatki inwestycyjne per capita,
- podmioty REGON na 10 tys. mieszkańców,
- bezrobocie, pracujący lub wynagrodzenia — zależnie od dostępnego poziomu,
- wyniki egzaminu ósmoklasisty,
- liczba szkół, placówek zdrowotnych i przystanków,
- dostęp do kolei i czas dojazdu do miasta powiatowego.

## Źródła

- BDL GUS: https://bdl.stat.gov.pl/
- API BDL: https://api.stat.gov.pl/Home/BdlApi
- TERYT: https://api.stat.gov.pl/Home/TerytApi
- PRNG: https://www.geoportal.gov.pl/pl/dane/panstwowy-rejestr-nazw-geograficznych-prng/
- wyniki egzaminu ósmoklasisty: https://stat.gov.pl/obszary-tematyczne/edukacja/edukacja/srednie-wyniki-uczniow-na-egzaminie-osmoklasisty,18,1.html

## Schemat analizy

1. Dołącz dane zewnętrzne do tabeli gmin.
2. Standaryzuj zmienne.
3. Porównaj PCA, t-SNE i UMAP.
4. Utwórz klastry i opisz je drzewem.
5. Zdefiniuj zewnętrzny target, np. saldo migracji, wynik edukacyjny lub dochody.
6. Porównaj model tabelaryczny z modelem rozszerzonym o cechy grafowe.
7. Zastosuj walidację grupową według województw, aby sprawdzić uogólnienie przestrzenne.

## Uwaga o interpretacji

Korelacja i ważność cechy nie oznaczają przyczynowości. Należy unikać leakage, np. nie wolno używać składnika indeksu jako predyktora tego samego indeksu bez jasnego oznaczenia, że model jest tylko surrogate.
