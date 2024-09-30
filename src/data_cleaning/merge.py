import pandas as pd
import numpy as np

df = pd.read_csv('../../data/raw/df.csv', encoding='utf-8')
df = df.where(pd.notnull(df), None)
df_income = pd.read_csv('../../data/raw/taxable_income_full.csv', encoding='utf-8')

df['region_code'] = df['region_code'].astype(float)
df_income['region_code'] = df_income['region_code'].astype(float)

merged_df = pd.merge(df, df_income[['year', 'region_code', 'taxable_income']], on=['year', 'region_code'], how='left')

merged_df.to_csv('../../results/merged_df.csv', index=False, encoding='utf-8-sig')

print(df.dtypes)
print("----")
print(df_income.dtypes)
print("----")
print(merged_df.dtypes)