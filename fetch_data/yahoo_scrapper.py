import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker="AAPL", period="1mo", interval="1d"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)
    df.reset_index(inplace=True)
    return df

# Example usage
if __name__ == "__main__":
    data = fetch_stock_data("TSLA")
    print(data.head())
