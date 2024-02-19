import numpy as np


def autocorrelation(data:np.ndarray, tau):
    assert data.ndim == 2
    count = len(data)-1
    t = len(data[0])-1

    assert tau < t

    _data = data.T

    return np.mean(_data[t] * _data[t-tau])


def autocorrelation_seq(data:np.ndarray):
    assert data.ndim == 2
    count = len(data)-1
    t = len(data[0])-1

    seq = []
    for i in range(t):
        seq.append(autocorrelation(data, i))

    return np.array(seq)