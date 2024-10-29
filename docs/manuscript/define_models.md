# モデルの定義

## 固定効果モデル

$$
\begin{array}{rcl}
    \mu_{it} = \beta \text{Bridge}_{it} + X^T_{it} \gamma + \text{Islands}_i + \text{Year}_t + \epsilon_{it} \\
\end{array}
$$

$$
\begin{array}{rcl}
    \beta &\sim & \operatorname{Normal}(0,~100)\\
    \gamma &\sim & \operatorname{Normal}(0,~100)\\
    \delta\_islands &\sim & \operatorname{Normal}(0,~100)\\
    \delta\_years &\sim & \operatorname{Normal}(0,~100)\\
    \sigma &\sim & \operatorname{InverseGamma}(0.001,~0.001)\\\text{Population} &\sim & \operatorname{Normal}(\mu,~\sigma)
\end{array}
$$

## GLMM

$$
Population_{it} \sim NegBin(\mu_{it}, \phi) \\

\mu_{it} = \alpha + \beta \times Bridge_{it} + X^T_{it} \gamma + u_{i} + \epsilon_{it} \\

u_{i} \sim N(0, \sigma^2_u) \\
$$
