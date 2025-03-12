# database.py

import sqlite3

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('cerion.db')  # Connecting to an SQLite database
    conn.row_factory = sqlite3.Row  # Allows returning rows as dictionaries
    return conn

# Example function to create a table
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create a table for storing trades (simplified example)
    cursor.execute('''CREATE TABLE IF NOT EXISTS trades (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        coin_name TEXT,
                        amount REAL,
                        price REAL,
                        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

# Function to add a trade (for example)
def add_trade(coin_name, amount, price):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO trades (coin_name, amount, price)
                      VALUES (?, ?, ?)''', (coin_name, amount, price))
    conn.commit()
    conn.close()
