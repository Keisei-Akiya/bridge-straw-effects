# モデルの定義

## TWFE

classic

$$
log{Y_{it}} = \delta T_{it} + \text{island}_i + \text{year}_t + \epsilon_{it}
$$

bayes

$$
\begin{aligned}
\log{Y_{it}} &\sim \mathcal{t}(\nu=3, \mu_{it}, \sigma^2) \\
\mu_{it} &= \alpha + \beta T_{it} + \text{island}_i + \text{year}_t \\
\sigma &\sim \text{Half-}\mathcal{t}(\nu=3, 1) \\
\alpha &\sim \mathcal{N}(0,1) \\
\beta &\sim \mathcal{N}(0,1) \\
\text{island}_i &\sim \mathcal{N}(\mu_{\text{island}}, \sigma_{\text{island}}) \\
\text{year}_t &\sim \mathcal{N}(\mu_{\text{year}}, \sigma_{\text{year}}) \\
\sigma_{\gamma} &\sim \text{Half-}\mathcal{t}(\nu=3, 1) \\
\mu_{\text{island}} &\sim \mathcal{N}(0, 1) \\
\sigma_{\text{island}} &\sim \text{Half-}\mathcal{t}(\nu=3, 1) \\
\mu_{\text{year}} &\sim \mathcal{N}(0, 1) \\
\sigma_{\text{year}} &\sim \text{Half-}\mathcal{t}(\nu=3, 1) \\
\end{aligned}
$$

## Dynamic TWFE

classic

$$
Y_{it} = \sum_{l \in L} \delta_l \mathbf{1}[t - k_i = l] + \text{island}_i + \text{year}_t +  \epsilon_{it}
$$

bayes

$$

\begin{aligned}
\log{Y_{it}} &\sim \mathcal{t}(\nu=3, \mu_{it}, \sigma^2) \\
\mu_{it} &= \alpha + (\beta + \gamma_{\ell}) T_{it} + \text{island}_i + \text{year}_t \\
\sigma &\sim \text{Half-}\mathcal{t}(\nu=3, \sigma=1) \\
\alpha &\sim \mathcal{N}(0, 1) \\
\beta &\sim \mathcal{N}(0, 1) \\
\gamma_{\ell} &\sim \mathcal{N}(\mu_{\gamma}, \sigma_{\gamma}) \\
\text{island}_i &\sim \mathcal{N}(\mu_{\text{island}}, \sigma_{\text{island}}) \\
\text{year}_t &\sim \mathcal{N}(\mu_{\text{year}}, \sigma_{\text{year}}) \\
\mu_{\gamma} &\sim \mathcal{N}(0, 1) \\
\sigma_{\gamma} &\sim \text{Half-}\mathcal{t}(\nu=3, 1) \\
\mu_{\text{island}} &\sim \mathcal{N}(0, 1) \\
\sigma_{\text{island}} &\sim \text{Half-}\mathcal{t}(\nu=3, 1) \\
\mu_{\text{year}} &\sim \mathcal{N}(0, 1) \\
\sigma_{\text{year}} &\sim \text{Half-}\mathcal{t}(\nu=3, 1) \\
\end{aligned}
$$

## Fully-saturated TWFE

classic

$$
Y_{it} = \sum_{k \notin C}\sum_{l \in L} \delta_{lk} \mathbf{1}[G_k=k]\mathbf{1}[t-k=l] + \text{island}_i + \text{year}_t + \epsilon_{it}
$$

bayes

$$
\begin{aligned}
\log{Y_{it}} &\sim \mathcal{t} (\nu=3, \mu_{it}, \sigma^2) \\
\mu_{it} &= \alpha + (\beta + {\gamma}_{k,\ell}) T_{it} + \text{island}_i + \text{year}_t \\
\sigma &\sim \text{Half-}\mathcal{t}(\nu=3, 1) \\
\alpha &\sim \mathcal{N}(0, 1) \\
\beta &\sim \mathcal{N}(0, 1) \\
\gamma_{k,\ell} &\sim \mathcal{N}(\mu_{\gamma}, \sigma_{\gamma}) \\
\text{island}_i &\sim \mathcal{N}(\mu_{\text{island}}, \sigma_{\text{island}}) \\
\text{year}_t &\sim \mathcal{N}(\mu_{\text{year}}, \sigma_{\text{year}}) \\
\mu_{\gamma} &\sim \mathcal{N}(0, 1) \\
\sigma_{\gamma} &\sim \text{Half-}\mathcal{t}(\nu=3, 1) \\
\mu_{\text{island}} &\sim \mathcal{N}(0, 1) \\
\sigma_{\text{island}} &\sim \text{Half-}\mathcal{t}(\nu=3, 1) \\
\mu_{\text{year}} &\sim \mathcal{N}(0, 1) \\
\sigma_{\text{year}} &\sim \text{Half-}\mathcal{t}(\nu=3, 1) \\
\end{aligned}
$$

## 一般化合成コントロール法

基本モデル

$$
Y_{it} = \delta_{it} D_{it} + X_{it}^⊤ \beta + \lambda_i^⊤ f_t + \epsilon_{it}
$$

- $Y_{it}$: 人口
- $\delta_{it}$: 処置効果
- $D_{it}$: 処置の有無を示すダミー変数
- $X_{it}$: 観測可能な共変量
- $\beta$: 共変量の係数
- $f_t$: 潜在因子 (時点に依存する未観測要因，事前分布を与える)．
- $\lambda_i$: 因子負荷量 (単位ごとの感受性，事前分布を与える)．
- $\epsilon_{it}$: 誤差項

1. アウトカムの分布

   $$
   Y_{it} \sim \mathcal{N}(\mu_{it}, \sigma)
   $$

   平均 $\mu_{it}$ の定義

   $$
   \mu_{it} = \delta_{it} D_{it} + X_{it}^⊤ \beta + \lambda_i^⊤ f_t
   $$

2. 潜在因子

   $$
   f_t \sim \mathcal{N}(0, \sigma_f^2)
   $$

3. 因子負荷量

   $$
   \lambda_i \sim \mathcal{N}(0, \sigma_{\lambda}^2)
   $$

4. 共変量の係数

   $$
   \beta \sim \mathcal{N}(0, \sigma_{\beta}^2)
   $$

5. 誤差項の分散

   $$
   \sigma \sim \mathcal{Cauchy}^+(1)
   $$

制約条件

1. スケーリング

   潜在因子と因子負荷量のスケールを制約しないと，推定が不安定になるため，正規化条件を課す．

   $$
   \sum_{t} f_{t}^2 = 1 \\
   \sum_{i} \lambda_{i}^2 = 1 \\
   $$

2. 因子数の選択
