import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def plot_moving_average(symbol, window=20, return_fig=False):
    conn = sqlite3.connect("stocks.db")
    df = pd.read_sql_query(f'''
        SELECT * FROM stocks_data WHERE symbol = ? ORDER BY date
    ''', conn, params=(symbol,))
    conn.close()

    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df['MA'] = df['close'].rolling(window=window).mean()

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df['close'], label='Close Price')
    ax.plot(df['MA'], label=f'{window}-Day MA', linestyle='--')
    ax.set_title(f"{symbol} - {window}-Day Moving Average")
    ax.legend()
    ax.grid()

    if return_fig:
        return fig
    else:
        plt.show()

# Example
plot_moving_average('AAPL', window=20)
