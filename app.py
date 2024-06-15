from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'financial_data.db'

@app.route('/')
def index():
    # Connect to the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Example: Fetch transactions from SQLite database
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()

    # Close the connection
    conn.close()

    # Render template with context
    return render_template('index.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)
