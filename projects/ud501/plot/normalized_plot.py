import pandas as pd
import matplotlib.pyplot as plt

def get_data(symbols):
    dates = pd.date_range('2010-01-01', '2010-12-31')
    df = pd.DataFrame(index=dates)

    for symbol in symbols:

        df_temp = pd.read_csv("../data/{}.csv".format(symbol), 
            index_col="Date", 
            parse_dates=True, 
            usecols=["Date", "Adj Close"],
            na_values=["nan"])
        df_temp = df_temp.rename(columns = {"Adj Close":symbol})
        df = df.join(df_temp, how="inner")
        
    return df

def normalize_data(df):
    return df / df.ix[0,:]
    

def main():
    symbols = ["AAPL", "IBM", "SPY", "GOOG"]
    df = get_data(symbols)
    df = normalize_data(df)
    df.plot()
    plt.show()

main()