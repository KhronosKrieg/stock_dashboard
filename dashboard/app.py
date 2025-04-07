import streamlit as st
from fetch_data.yahoo_scraper import fetch_stock_data
import plotly.graph_objects as go

st.title("📈 Stock Market Analyzer")

ticker = st.text_input("Enter stock symbol (e.g. AAPL)", value="AAPL")
data = fetch_stock_data(ticker)

st.write("### Price Chart")
fig = go.Figure(data=[go.Candlestick(
    x=data['Date'],
    open=data['Open'],
    high=data['High'],
    low=data['Low'],
    close=data['Close'])])
st.plotly_chart(fig)

st.write("### Raw Data")
st.dataframe(data)
