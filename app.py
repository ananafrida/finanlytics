from flask import Flask, render_template, g
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.io as pio
import os

app = Flask(__name__)

DATABASE = 'financial_data.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

@app.teardown_appcontext
def close_db(error):
    if 'db' in g:
        g.db.close()

@app.route('/')
def index():
    # Connect to the database
    conn = get_db()
    cursor = conn.cursor()

    # Fetch transactions
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()

    # Perform data analysis
    df = pd.DataFrame(transactions, columns=['id', 'date', 'amount', 'category', 'description'])
    df['date'] = pd.to_datetime(df['date'])
    df.fillna(0, inplace=True)

    # Aggregate data by category
    category_summary = df.groupby('category')['amount'].sum().reset_index()

    # Monthly expenditure trend
    df['month'] = df['date'].dt.to_period('M').astype(str)  # Convert Period to string
    monthly_summary = df.groupby('month')['amount'].sum().reset_index()

    # Create Plotly plots
    category_fig = px.bar(category_summary, x='category', y='amount', title='Expenditure by Category')
    monthly_fig = px.line(monthly_summary, x='month', y='amount', title='Monthly Expenditure Trend')

    # Save plots to HTML divs
    category_plot_div = pio.to_html(category_fig, full_html=False)
    monthly_plot_div = pio.to_html(monthly_fig, full_html=False)

    return render_template('index.html', transactions=transactions, category_plot_div=category_plot_div, monthly_plot_div=monthly_plot_div)

if __name__ == '__main__':
    app.run(debug=True)
