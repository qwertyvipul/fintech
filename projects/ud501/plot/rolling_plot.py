import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)
    
    for symbol in symbols:
        df_temp = pd.read_csv("../data/{}.csv".format(symbol),
                             index_col = "Date",
                             parse_dates=True,
                             usecols=["Date", "Adj Close"],
                             na_values=["nan"])
        df_temp = df_temp.rename(columns={"Adj Close":symbol})
        df = df.join(df_temp, how="inner")
    
    return df

def get_rolling_mean(data, window):
    return pd.rolling_mean(data, window = window)

def get_rolling_std(data, window):
    return pd.rolling_std(data, window = window)

def get_bollinger_bands(rolling_mean, rolling_std):
    upper_band = rolling_mean + 2 * rolling_std
    lower_band = rolling_mean - 2 * rolling_std
    return upper_band, lower_band

dates = pd.date_range('2010-01-01', '2010-12-31')
symbols = ["SPY"]

df = get_data(symbols, dates)
rolling_mean = get_rolling_mean(df["SPY"], 20)
rolling_std = get_rolling_std(df["SPY"], 20)
upper_band, lower_band = get_bollinger_bands(rolling_mean, rolling_std)

ax = df['SPY'].plot(title="Bollinger Bands", label="SPY")
rolling_mean.plot(label="Rolling Mean", ax = ax)
upper_band.plot(label="Upper Band", ax = ax)
lower_band.plot(label="Lower Band", ax = ax)

ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.legend(loc="Upper Left")
plt.show()