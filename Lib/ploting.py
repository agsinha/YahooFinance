import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_Divideds(data,tik):
    # Convert 'Date' column to datetime
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'], utc=True)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Dividends'])

    # Format the date on x-axis
    date_formatter = mdates.DateFormatter('%Y-%m')
    ax.xaxis.set_major_formatter(date_formatter)
    plt.gcf().autofmt_xdate()

    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title("Dividends Paid: " + tik)
    plt.grid(True)
    plt.show()
