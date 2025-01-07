import pandas as pd
import numpy as np
import pymc as pm
import arviz as az
rng = np.random.default_rng(42)

# Load data
path = '../../data/processed/df_filtered.xlsx'
df = pd.read_excel(path)

log_pop_star_scaled = df['log_pop_star'] / 2 / df['log_pop_star'].std()

# Model
# 0から始まるインデックスを振り直す
island_ids, unique_island_ids = pd.factorize(df['island_ids'])
n_islands = len(unique_island_ids)
bridge_year, unique_bridge_year = pd.factorize(df['bridge_year'])
n_bridge_year = len(unique_bridge_year)
time_since_treatment, unique_time_since_intervention = pd.factorize(df['time_since_treatment'])
n_time_since_intervention = len(unique_time_since_intervention)

COORDS = {'obs_id': df.index}

with pm.Model(coords=COORDS) as model_h_hetero:
    # data
    island_ids = pm.Data('island_ids', island_ids)
    bridge_year = pm.Data('bridge_year', bridge_year)
    treatment_group = pm.Data('treatment_group', df['treatment_group'])
    time_since_treatment = pm.Data('time_since_treatment', time_since_treatment)

    # priors
    # ATT
    mu_beta = pm.Normal('mu_beta', mu=0, sigma=1)
    sigma_beta = pm.HalfCauchy('sigma_beta', 1)
    z_beta = pm.Normal('z_beta', mu=0, sigma=1, shape=(n_bridge_year, n_time_since_intervention))
    beta = pm.Deterministic('beta', mu_beta + sigma_beta * z_beta)

    # sigma
    sigma_global = pm.HalfCauchy('sigma_global', 1)
    sigma = pm.HalfCauchy('sigma', sigma_global, shape=n_islands)

    # fixed effects
    alpha = pm.Normal('alpha', mu=0, sigma=1)
    nu = 7

    # expected value
    mu = alpha + beta[bridge_year, time_since_treatment] * treatment_group

    # likelihood
    y_obs = pm.StudentT('y_obs', mu=mu, sigma=sigma[island_ids], nu=nu, observed=log_pop_star_scaled, dims='obs_id')

    # sampling
    trace_h_hetero = pm.sample(3000, tune=1000, target_accept=.9, random_seed=rng, nuts_sampler='numpyro')

az.to_netcdf(trace_h_hetero, './mcmc_sample/fully_saturated/hie_hetero.nc')