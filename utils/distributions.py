import numpy as np
from scipy.stats import invgamma


def sample_gaus(_mu0, _n, _mean, _sigma2, _sigma02):
    dom = _sigma2 + _n * _sigma02
    return np.random.normal(loc=(_sigma2 * _mu0 + _sigma02 * _n * _mean) / dom, scale=np.sqrt(_sigma2 * _sigma02) / dom,
                            size=1)


def sample_invGa(_alpha, _beta, _n, _mean):
    return invgamma.rvs(_alpha + _n / 2, scale=_beta + _n * _mean / 2, size=1)


def gibbs_sample(mean_, sigma2_, n_, samples, alpha_=10, beta_=0.5, sigma_02=100):
    mu = mean_
    sigma2 = sigma2_

    mu_0 = mu
    sigma_02 = sigma_02

    alpha = alpha_
    beta = beta_

    mu_L = []
    sigma2_L = []

    for i in range(samples):
        mu = sample_gaus(mu_0, n_, mean_, sigma2, sigma_02)
        sigma2 = sample_invGa(alpha, beta, n_, mean_)

        mu_L += [mu]
        sigma2_L += [sigma2]

    mu_L = np.array(mu_L).squeeze()
    sigma2_L = np.array(sigma2_L).squeeze()
    index = np.arange(len(mu_L))

    return mu_L, sigma2_L, index


def gibbs_samplings(mean_, sigma2_, n_, samples, realization_count):
    mu_T = []
    sigma2_T = []

    for i in range(realization_count):
        _mu_L, _sigma2_L, _ = gibbs_sample(mean_, sigma2_, n_, samples)

        mu_T += [_mu_L]
        sigma2_T += [_sigma2_L]

        if (i + 1) % 10 == 0:
            print(f'{i + 1} / {realization_count}')

    mu_T = np.array(mu_T)
    sigma2_T = np.array(sigma2_T)

    return mu_T, sigma2_T
