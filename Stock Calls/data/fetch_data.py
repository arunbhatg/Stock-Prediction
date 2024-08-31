import yfinance as yf
import os
import pandas as pd

def fetch_stock_data(symbol, start_date, end_date, cache_file='data/sample_data.csv'):
    if os.path.exists(cache_file):
        return pd.read_csv(cache_file, index_col='Date', parse_dates=True)
    
    try:
        df = yf.download(symbol, start=start_date, end=end_date)
        df.to_csv(cache_file)
        return df
    except Exception as e:
        print(f"Failed to fetch data: {e}")
        return None

if __name__ == "__main__":
    symbol = 'RELIANCE.NS'
    data = fetch_stock_data(symbol, '2023-01-01', '2023-08-01')
    print(data.head())
