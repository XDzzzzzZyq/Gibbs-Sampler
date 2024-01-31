import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

import pandas as pd


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
