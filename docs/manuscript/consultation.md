# 相談

- 2 つのコブ問題が解決した
- 平行トレンドの仮定が成立しているかどうか
- 島別の不均一分散をやってみようと思うがどうか
- Dynamic TWFE の結果
- Fully saturated の結果のグラフの見せ方

## 2 つのコブ問題が解決した

島・年平均をそのまま引くケース

$$
\log{Y_{it}}^* = \log{Y_{it}} - \bar{\log{Y_{i}}} - \bar{\log{Y_{t}}}
$$

島平均を引いてから，島平均を引いた後の年平均を引くケース

$$
\begin{aligned}
\log{Y_{it}}^* &= \log{Y_{it}} - \bar{\log{Y_{i}}} \\
\log{Y_{it}}^{**} &= \log{Y_{it}}^* - \bar{\log{Y_{t}}}^* \\
\end{aligned}
$$

![変換済み対数人口](../figures/converted_logarithmic_population.png)

## 平行トレンドの仮定が成立しているかどうか

![平行トレンド](../figures/parallel_trend.png)

## 不均一分散をやってみようと思うがどうか

$$
\begin{aligned}
\log{Y_{it}}^{**} &\sim \mathcal{t} (\nu, \mu_{it}, \sigma_i^2) \\
\sigma_i &\sim \mathcal{Cauchy}^+(\sigma_{\text{global}}^2) \\
\sigma_{\text{global}} &\sim \mathcal{Cauchy}^+(1) \\
\end{aligned}
$$

誤差分散が島ごとに異なるということ．

![不均一分散](../figures/twfe/twfe_heteroskedasticity.png)

## Dynamic TWFE の結果

![Dynamic TWFEの結果](../figures//dynamic_twfe/att_over_time_hie_hetero_const.png)

## Fully saturated の結果のグラフの見せ方
