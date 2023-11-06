import yfinance as yf

"""
    This library is used for scraping technical(statistical) data
    from Yahoo Finanace.
"""

def get_tch_dataframe(symbol, period="max"):
    
    # Get data on this ticker
    tickerData = yf.Ticker(symbol)

    # Get the historical prices for this ticker
    tickerDf = tickerData.history(period=period)

    return tickerDf


def output_csv(name, df):
    
    # Dataframe to csv
    df.to_csv(f"Datasets/{name}.csv")