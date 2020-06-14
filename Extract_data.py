import os
import yfinance as yf
import datetime as dt
from dateutil.relativedelta import relativedelta


class Extraction:
    """A class for extracting data from Yahoo finance"""

    def __init__(self, ticker, col, dir):
        self.ticker = ticker
        self.column = col
        self.dir = dir

    def get_historical_data_50Y(self, start_date, end_date):
        data = yf.download(self.ticker, start_date, end_date)[self.column]
        ret = data.pct_change(1)
        ret.dropna(how='any', inplace=True)
        ret.to_csv(os.path.join(self.dir, 'data_50Y.csv'))

    def get_historical_data_1Y(self):
        start_date = dt.datetime.now() - relativedelta(months=11)
        start_date = start_date.replace(day=1)
        end_date = dt.datetime.now()
        data = yf.download(self.ticker, start_date, end_date)[self.column]
        ret = data.pct_change(1)
        ret.dropna(how='any', inplace=True)
        ret.to_csv(os.path.join(self.dir, 'data_1Y.csv'))
