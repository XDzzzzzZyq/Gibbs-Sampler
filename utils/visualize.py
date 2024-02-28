import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

import pandas as pd
import numpy as np


def draw(data, title="BTC", xlabel="Date", ylabel=""):
    sns.set_style("darkgrid")
    plt.figure(figsize=(15, 6))
    plt.plot(data)
    # plt.xticks(range(0,data.shape[0],20), data['Date'].loc[::20], rotation=45)
    plt.title(title, fontsize=18, fontweight='bold')

    locator = mdates.DayLocator(interval=100)
    plt.gca().xaxis.set_major_locator(locator)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    plt.gcf().autofmt_xdate()
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    plt.show()


def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # the scatter plot:
    ax.scatter(x, y)

    # now determine nice limits by hand:

    binsx = np.linspace(min(x), max(x), num=40).squeeze()
    binsy = np.linspace(min(y), max(y), num=40).squeeze()
    ax_histx.hist(x, bins=binsx)
    ax_histy.hist(y, bins=binsy, orientation='horizontal')


def show_distribution(mu, sigma2):
    # Start with a square Figure.
    fig = plt.figure(figsize=(12, 12))
    # Add a gridspec with two rows and two columns and a ratio of 1 to 4 between
    # the size of the marginal axes and the main axes in both directions.
    # Also adjust the subplot parameters for a square plot.
    gs = fig.add_gridspec(2, 2, width_ratios=(4, 1), height_ratios=(1, 4),
                          left=0.1, right=0.9, bottom=0.1, top=0.9,
                          wspace=0.05, hspace=0.05)
    # Create the Axes.
    ax = fig.add_subplot(gs[1, 0])
    ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
    ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)
    # Draw the scatter plot and marginals.
    scatter_hist(mu, sigma2, ax, ax_histx, ax_histy)

    ax.set_xlabel(r'Distribution of $\mu$')
    ax.set_ylabel(r'Distribution of $\sigma^2$')


import statsmodels.api as sm
from statsmodels.graphics import tsaplots


def show_corr(data):
    mu_ac = sm.tsa.acf(data, nlags=100)
    plt.figure(figsize=(12, 4))
    plt.plot(range(len(mu_ac)), mu_ac)
    plt.xlabel(r"lags $\tau$")
    plt.show()


def show_VaR(data, var):
    bins = np.linspace(data.min(), data.max(), 50)
    plt.figure(figsize=(12, 6))
    plt.hist(data, bins=bins, label='Log Returns')
    plt.axvspan(min(var), max(var), color='k', label='99% VaR', alpha=0.5)
    plt.legend()
    plt.show()

def show_VaR_ES(data, var, es):
        bins = np.linspace(data.min(), data.max(), 50)
        plt.figure(figsize=(12, 6))
        plt.hist(data, bins=bins, label='Log Returns')
        plt.axvspan(min(var), max(var), color='k', label='99% VaR', alpha=0.5)
        plt.axvspan(min(es), max(es), color='r', label='99% ES', alpha=0.5)
        plt.legend()
        plt.show()
