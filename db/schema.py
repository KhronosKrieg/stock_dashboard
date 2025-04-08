import sqlite3

def create_stock_table():
    conn = sqlite3.connect("stocks.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stocks_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT,
            date DATE,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume INTEGER,
            PRIMARY KEY (symbol, date)  -- ensures no duplicate for same symbol & date
            )
        ''')
    conn.commit()
    conn.close()
