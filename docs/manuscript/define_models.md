# モデルの定義

## 個体・時間ランダム効果

$$
\begin{aligned}
\log{Y_{it}^*} &= \log{Y_{it}} - \bar{\log{Y}_i} \\
\log{Y_{it}^{**}} &= \log{Y_{it}^*} - \bar{\log{Y}^*_t} \\
\end{aligned}
$$

- $\log{Y_{it}}$: 観測値
- $\bar{\log{Y}_i}$: 個体 $i$ の平均値
- $\log{Y_{it}^*}$: 個体固定効果を除いた値
- $\bar{\log{Y}^*_t}$: 個体固定効果を除いた値の時間 $t$ の平均値
- $\log{Y_{it}^{**}}$: 個体と時間の固定効果を除いた値

## Two way Fixed Effects

$$
\begin{aligned}
\log{Y_{it}^{**}} &\sim \mathcal{t} (\nu, \mu_{it}, \sigma_i^2) \\
\nu &\sim \text{Exponential}(1/10) \\
\mu_{it} &= \beta \cdot W_{it}\\
\beta &\sim \mathcal{N}(0, 1) \\
\sigma_i &\sim \mathcal{C}^+(\sigma_0^2) \\
\end{aligned}
$$

- $i$: 島
- $t$: 年
- $\nu$: $\mathcal{t}$ 分布の自由度パラメータ
- $\beta$: 介入効果
- $W_{it}$: 介入後に 1 を取るダミー変数
- $\sigma_i^2$: 島 $i$ の誤差分散
- $\sigma_0^2$: 島間の誤差分散を表すハイパーパラメータ

介入効果 $\beta$ の事前分布は平均 0，分散 1 の正規分布を仮定している．被説明変数は対数であるため，パラメータが現実的に取りうる値は，-1 から 1 の範囲に収まるだろう．パラメータが-1 の場合，島の人口が居なくなったことを意味し，パラメータが 1 の場合，島の人口が倍になったことを意味するからだ．したがって現実的に取りうる推定値より少し広い範囲で事前分布を設定している．

島間の誤差分散を表すハイパーパラメータ $\sigma_0^2$ は スケールパラメータ 1 の半コーシー分布としている．分散は 0 以上の値を取るため，そのように制約を設けている．スケールパラメータの値だが，被説明変数は対数故にそれほど大きな分散を持たないと考えられるため，1 としている．

$\sigma_i^2$ は島ごとに誤差分散が異なることを仮定している．

![島別人口 (固定効果排除済み) の標準偏差 ヒストグラム](../figures/stdev_of_logpop_by_island.png)

固定効果を排除した島別人口の対数値の標準偏差をヒストグラムで示している．人口が多い島や，人口が少ない島が混在しているため，島ごとに誤差分散が異なると考えられる．

## Dynamic TWFE

$$
\begin{aligned}
\log{Y_{it}^{**}} &\sim \mathcal{t} (\nu, \mu_{it}, \sigma_i^2) \\
\nu &\sim \text{Exponential}(1/10) \\
\mu_{it} &= \beta_l \cdot T_{i}\\
\beta_l &\sim \mathcal{N}(\mu_{\beta}, \sigma_{\beta}^2) \\
\sigma_i &\sim \mathcal{C}^+(\sigma_0^2) \\
\end{aligned}
$$

- $\beta_l$: 介入の経過年数 $l$ における介入効果
- $T_{i}$: 介入群ならば 1 を取るダミー変数
- $\mu_{\beta}$: 経過年数間の平均を表すハイパーパラメータ
- $\sigma_{\beta}^2$: 経過年数間の分散を表すハイパーパラメータ

$\beta_l$ は介入の経過年数によって効果が異なる事を考慮している．経過年数 $l$ は介入年を $0$ とし，介入前は負の値，介入後は正の値を取る．これは，橋を架ける前や架けた後，時間が経つにつれてその効果がどのように変化するかを観察するためである．

$\beta_l$ に関する平均と分散のハイパーパラメータは $\mu_{\beta} \sim \mathcal{N}(0, 1)$ ， $\sigma_{\beta} \sim \mathcal{C}^+(1)$ としている．

## Fully Saturated TWFE

$$
\begin{aligned}
\log{Y_{it}^{**}} &\sim \mathcal{t} (\nu, \mu_{it}, \sigma_i^2) \\
\nu &\sim \text{Exponential}(1/10) \\
\mu_{it} &= \beta_{g, l} \cdot T_{i} \\
\beta_{g, l} &\sim \mathcal{N}(\mu_{\beta}, \sigma_{\beta}^2) \\
\sigma_i &\sim \mathcal{C}^+(\sigma_0^2) \\
\end{aligned}
$$

- $\beta_{g, l}$: 介入時期 $g$ における経過年数 $l$ における介入効果
- $T_{i}$: 介入群ならば 1 を取るダミー変数
- $\mu_{\beta}$: 介入時期間，経過年数間の平均を表すハイパーパラメータ
- $\sigma_{\beta}^2$: 介入時期間，経過年数間の分散を表すハイパーパラメータ

$\beta_{g, l}$ は介入時期によって介入効果は異なるということを考慮している．架橋には優先順位があり，介入時期が早い島と遅い島では，介入効果が異なるはずである．
