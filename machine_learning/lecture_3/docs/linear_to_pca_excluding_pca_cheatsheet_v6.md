
# Ściąga v6: wzory z bloku design matrix → odds → logistic → ROC → regularyzacja

## Model liniowy

$$
y=X\beta+\varepsilon
$$

$$
\hat\beta=(X^TX)^{-1}X^Ty
$$

$$
SSE=\sum_i(y_i-\hat y_i)^2
$$

Porównanie modeli liniowych:

$$
F=\frac{(SSE_{reduced}-SSE_{full})/(k_{full}-k_{reduced})}{SSE_{full}/(n-k_{full})}
$$

Dla dwóch grup:

$$
F=t^2
$$

## Odds i logit

$$
odds=\frac{p}{1-p}
$$

$$
logit(p)=\log\left(\frac{p}{1-p}\right)
$$

$$
p=\frac{1}{1+e^{-z}}
$$

## Odds ratio

Dla tabeli:

$$
\begin{array}{c|cc}
 & Yes & No \\
\hline
Group\ 1 & a & b \\
Group\ 2 & c & d
\end{array}
$$

$$
OR=\frac{a/b}{c/d}=\frac{ad}{bc}
$$

$$
\log(OR)=\log\left(\frac{ad}{bc}\right)
$$

$$
SE(\log OR)=\sqrt{\frac1a+\frac1b+\frac1c+\frac1d}
$$

$$
z=\frac{\log(OR)}{SE(\log OR)}
$$

## Regresja logistyczna

$$
P(y=1|x)=\sigma(x^T\beta)
$$

$$
\ell(\beta)=\sum_i \left[y_i x_i^T\beta-\log(1+e^{x_i^T\beta})\right]
$$

$$
NLL=-\ell
$$

Likelihood-ratio test:

$$
G^2=2(\ell_{full}-\ell_{reduced})
$$

McFadden pseudo-$R^2$:

$$
R^2_{McFadden}=1-\frac{\ell_{full}}{\ell_{null}}
$$

## ROC/AUC

$$
TPR=\frac{TP}{TP+FN}
$$

$$
FPR=\frac{FP}{FP+TN}
$$

Pairwise AUC:

$$
AUC=\frac{\#(score_+>score_-)+0.5\#(score_+=score_-)}{n_+n_-}
$$

## Regularyzacja

Ridge:

$$
Loss+\lambda\sum_{j>0}\beta_j^2
$$

Lasso:

$$
Loss+\lambda\sum_{j>0}|\beta_j|
$$

Elastic Net:

$$
Loss+\lambda\left(\alpha\sum_{j>0}|\beta_j|+\frac{1-\alpha}{2}\sum_{j>0}\beta_j^2\right)
$$

Soft-thresholding:

$$
S(z,\gamma)=sign(z)\max(|z|-\gamma,0)
$$
