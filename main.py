import json
from db.schema import create_stock_table
from fetch_data.stocks import fetch_and_store_yfinance

if __name__ == "__main__":
    create_stock_table()

    # Fetch data for sample stocks
    #fetch_and_store_yfinance("AAPL")
    #fetch_and_store_yfinance("INFY.NS")

    with open("symbols.json", "r") as f:
        data = json.load(f)

    for symbol in data["stocks"]:
        fetch_and_store_yfinance(symbol)
