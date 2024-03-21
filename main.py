# This is a sample Python script.
import json
from Lib.buy import Buy
from Lib.ploting import plot_Divideds
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

if __name__ == '__main__':
    x = Buy("MSFT")
    #print(json.dumps(x.div, indent=2))
    #print(x.div)
    cp_divideds = pd.DataFrame(x.div)
    # Multi-Index Column proble with cp_divideds. See solution
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.xs.html
    #cp_divideds = cp_divideds.xs('Date')

    #print(column_names)
    column_names = cp_divideds.columns.values.tolist()
    cp_divideds.to_csv('outputs/divideds.csv')
    #df = pd.read_csv('outputs/divideds.csv')
    df = pd.read_csv('outputs/divideds.csv')
    plot_Divideds(df, x.symbol.ticker)
    #df.plot()
    #ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
    #fig.autofmt_xdate()

    #plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
