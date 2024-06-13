# filename: nvda_chart.py

import yfinance as yf
import matplotlib.pyplot as plt

def fetch_data(ticker_symbol):
    ticker_yahoo = yf.Ticker(ticker_symbol)
    return ticker_yahoo.history(period="1mo")

def plot_data(df, ticker_symbol):
    plt.figure(figsize=(14, 8))
    plt.plot(df['Close'])
    plt.title(f'{ticker_symbol} Stock Price Performance Last 30 Days', fontsize=20)
    plt.xlabel('Date', fontsize=16)
    plt.ylabel('Closing Price (USD)', fontsize=16)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    ticker_symbol = "NVDA"
    df = fetch_data(ticker_symbol)
    plot_data(df, ticker_symbol)