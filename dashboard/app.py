import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from fetch_data.stocks import fetch_and_store_yfinance
from export import export_stock_data
from analyze import plot_moving_average
import matplotlib.pyplot as plt

st.set_page_config(page_title="📈 Stock Analyzer", layout="wide")
st.title("📊 Personal Stock Dashboard")

# Input section
symbol = st.text_input("Enter stock symbol (e.g. AAPL)", "AAPL")

# Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔄 Refresh Data"):
        fetch_and_store_yfinance(symbol)
        st.success(f"Data refreshed for {symbol}")

with col2:
    if st.button("💾 Export to CSV"):
        export_stock_data(symbol, filetype="csv")

with col3:
    if st.button("📈 Show Moving Average Chart"):
        st.pyplot(plot_moving_average(symbol, return_fig=True))

