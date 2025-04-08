import sqlite3
import pandas as pd
from datetime import datetime

def export_stock_data(symbol, filetype="csv"):
    conn = sqlite3.connect("stocks.db")
    df = pd.read_sql_query(
        "SELECT * FROM stocks_data WHERE symbol = ? ORDER BY date",
        conn,
        params=(symbol,)
    )
    conn.close()

    if df.empty:
        print(f"No data found for symbol: {symbol}")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{symbol}_data_{timestamp}.{filetype}"

    if filetype == "csv":
        df.to_csv(filename, index=False)
        print(f"✅ Data exported to {filename}")
    elif filetype == "excel" or filetype == "xlsx":
        df.to_excel(filename, index=False)
        print(f"✅ Data exported to {filename}")
    else:
        print("❌ Unsupported file type. Use 'csv' or 'excel'.")

# Example usage
export_stock_data("AAPL", filetype="csv")
# export_stock_data("TSLA", filetype="excel")
