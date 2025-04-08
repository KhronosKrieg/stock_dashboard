import sqlite3

conn = sqlite3.connect("stocks.db")
cursor = conn.cursor()

# See what tables exist
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# Preview some data
cursor.execute("SELECT * FROM stocks_data LIMIT 10;")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
