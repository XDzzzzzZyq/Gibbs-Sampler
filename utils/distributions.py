import numpy as np
from scipy.stats import invgamma


def sample_gaus(_mu,_sigma2):
    return np.random.normal(loc=_mu, scale=np.sqrt(_sigma2), size=1)


def sample_invGa(_alpha, _beta):
    return invgamma.rvs(_alpha, scale=_beta, size=1)


def gibbs_sample(data, samples, alpha_=10, beta_=0.5, sigma_02=100):
    n_ = data.size
    mean_ = data.mean()
    sigma2_ = data.std()**2
    
    mu = mean_
    sigma2 = sigma2_

    mu_0 = mu
    sigma_02 = sigma_02

    alpha0 = alpha_
    beta0 = beta_
    V0 = sigma_02 / sigma2_
    Ex2 = sigma2_ - mean_**2

    mu_L = []
    sigma2_L = []

    for i in range(samples):

        Vn = sigma_02/(sigma2 + n_*sigma_02)
        mu_n = Vn/V0*mu_0 + Vn*n_*mean_        
        mu = sample_gaus(mu_n, sigma2*Vn)

        mu_s = ((data - mu)**2).sum()
        alpha_n = alpha0 + n_/2
        #beta_n = beta0 + (mu_0**2/V0 + n_*Ex2 - mu_n**2/Vn)/2
        beta_n = beta0 + mu_s/2
        
        sigma2 = sample_invGa(alpha_n, beta_n)

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
