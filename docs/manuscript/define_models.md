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
