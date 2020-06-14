import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


class Data_analysis:
    """A class for analyzing historical data of the S&P500"""

    def __init__(self, data_Y, data_M, dir):
        data_Y['Date'] = pd.to_datetime(data_Y['Date'])
        data_M['Date'] = pd.to_datetime(data_M['Date'])
        data_Y = data_Y.groupby(data_Y['Date'].dt.year)['Adj Close'].agg(['mean', 'count'])
        data_M = data_M.groupby([data_M['Date'].dt.year, data_M['Date'].dt.month])['Adj Close'].agg(['mean', 'count'])
        self.annualized_returns = data_Y['mean']*data_Y['count']
        self.monthly_returns = data_M['mean']*data_M['count']
        self.dir = dir

    def plot_annualized_returns(self):
        x = np.linspace(0, len(self.annualized_returns), len(self.annualized_returns))
        plt.figure(figsize=(12, 6))
        plt.scatter(x, self.annualized_returns)
        plt.axhline(y=0, color='r', linestyle='-')
        plt.xticks(x, self.annualized_returns.index, rotation=90, fontsize=9)
        plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
        plt.title('S&P 500 Annual Returns 1970 - 2019')
        plt.savefig(os.path.join(self.dir, 'S&P_500_historical_50Y_returns.png'), bbox_inches='tight', dpi=400)

        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        xname = []
        for i in range(len(months)):
            xname.append(months[self.monthly_returns.index[i][1]-1]+'\n'+str(self.monthly_returns.index[i][0]))
        x = np.linspace(0, len(self.monthly_returns), len(self.monthly_returns))
        plt.figure(figsize=(12, 7))
        plt.scatter(x, self.monthly_returns)
        plt.axhline(y=0, color='r', linestyle='-')
        plt.xticks(x, xname, fontsize=9)
        plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
        plt.title('S&P 500 Monthly Returns 2019 - 2020')
        plt.savefig(os.path.join(self.dir, 'S&P_500_historical_12M_returns.png'), bbox_inches='tight', dpi=400)

    def histogram_annualized_returns(self):
        ranges = [-1, -0.1, -0.05, 0, 0.05, 0.1, 0.15, 0.2, 1]
        histo = self.annualized_returns.groupby(pd.cut(self.annualized_returns, ranges)).count()/len(self.annualized_returns)
        barWidth = 0.8
        histo = histo.values.tolist()
        r1 = [1, 3, 5, 7, 9, 11, 13, 15]
        plt.figure(figsize=(12, 6))
        plt.bar(r1, histo, width=barWidth)
        plt.xticks(r1,
                   ['Less than 10%', 'Between -10%\nand -5%', 'Between -5%\nand 0%', 'Between 0%\nand 5%',
                    'Between 5%\nand 10%', 'Between 10%\nand 15%', 'Between 15%\nand 20%', 'Great than 20%'],
                   fontsize=9)
        for i in range(len(r1)):
            plt.text(x=r1[i] - 0.2, y=histo[i] + 0.002, s=str(round(histo[i], 3)*100)+'%', size=8)
        plt.title('S&P 500 Annual Return 1970 - 2019')
        plt.savefig(os.path.join(self.dir, 'S&P_500_histogram_50Y_returns.png'), bbox_inches='tight', dpi=400)

        histo = self.monthly_returns.groupby(pd.cut(self.monthly_returns, ranges)).count() / len(
            self.monthly_returns)
        histo = histo.values.tolist()
        plt.figure(figsize=(12, 6))
        plt.bar(r1, histo, width=barWidth)
        plt.xticks(r1,
                   ['Less than 10%', 'Between -10%\nand -5%', 'Between -5%\nand 0%', 'Between 0%\nand 5%',
                    'Between 5%\nand 10%', 'Between 10%\nand 15%', 'Between 15%\nand 20%', 'Great than 20%'],
                   fontsize=9)
        for i in range(len(r1)):
            plt.text(x=r1[i] - 0.2, y=histo[i] + 0.002, s=str(round(histo[i], 3) * 100) + '%', size=8)
        plt.title('S&P 500 Monthly Return 2019 - 2020')
        plt.savefig(os.path.join(self.dir, 'S&P_500_histogram_12M_returns.png'), bbox_inches='tight', dpi=400)

