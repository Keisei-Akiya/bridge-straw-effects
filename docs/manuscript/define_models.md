# モデルの定義

## Staggered DiD

### Sun and Abraham (JE, 2021)

1. Full data set に対して，Event timing グループを表すダミーとの交差項を入れた Event-study DiD を推定:
   $$
   Y_{it} = \text{islands}_i + \text{year}_t + \text{control}_{i} + \sum_{k \not\in C} \sum_{l \not ={-1}} \delta_{l,k} \mathbf{1}[G_k = k]\mathbf{1}[t-k=l] + \epsilon_{it}
   $$
2. Dynamic treatment effect $ATT_l$ を，次のように推定:
   $$
   ATT_l = \sum_k w_{l,k} \hat\delta_{l,k}
   $$
   - $w_{l,k}$:
     - 初期期間の重み．
   - $ATT_l$:
     - Event-study 推定量．
     - 全ての初期期間の真の処置効果の(一部負の)重み付け線形結合．

### Wooldridge (WP, 2021)

1. Full data set に対して，Event timing グループを表すダミーとの交差項を入れた Event-study DiD を推定:
   $$
   Y_{it} = \text{cohort}_k + \text{year}_t + \text{control}_{i} + \sum_{k \not\in C} \sum_{l > 0} \delta_{l,k} \mathbf{1}[G_k = k]\mathbf{1}[t-k=l] + \epsilon_{it}
   $$
   $\text{cohort}_k$は$\text{island}_i$でも良い．
2. Dynamic treatment effect $ATT_l$ を，次のように推定:
   $$
   ATT_l = \sum_k w_{l,k} \hat\delta_{l,k}
   $$
