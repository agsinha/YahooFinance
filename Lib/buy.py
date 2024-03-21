# https://pypi.org/project/yfinance/
import yfinance as yf

class Buy:
    "Provide stock data and key metrics to determine past performance of a stock"
    def __init__(self, symbol):
        tik  = yf.Ticker(symbol)
        self.symbol = tik
        self.actions = tik.actions
        self.div = tik.dividends
        self.splits= tik.splits
        self.capitalgains = tik.capital_gains  # only for mutual funds & etfs
        self.info= tik.info

    def __str__(self):
        #return f"{self.actions}({self.div})"
        return f"{self.div}"
