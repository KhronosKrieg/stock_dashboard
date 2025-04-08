import yfinance as yf
import sqlite3
from datetime import datetime

def fetch_and_store_yfinance(symbol, start="2023-01-01", end=None):
    if not end:
        end = datetime.today().strftime('%Y-%m-%d')

    df = yf.download(symbol, start=start, end=end, group_by='ticker')

    if df.empty:
        print(f"No data for {symbol}")
        return

    # Drop the 'Price' level in the columns
    df.columns = df.columns.droplevel(0)
    df = df.reset_index()

    conn = sqlite3.connect("stocks.db")
    cursor = conn.cursor()

    for _, row in df.iterrows():
        try:
            cursor.execute('''
                        INSERT INTO stocks_data (symbol, date, open, high, low, close, volume)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (
                symbol,
                row['Date'].strftime('%Y-%m-%d'),
                float(row['Open']),
                float(row['High']),
                float(row['Low']),
                float(row['Close']),
                int(row['Volume'])
            ))
        except sqlite3.IntegrityError:
            print(f"Duplicate entry skipped: {symbol} on {row['Date']}")

    conn.commit()
    conn.close()
    print(f"Inserted {len(df)} rows for {symbol}")
