from data.fetch_data import fetch_stock_data
from models.strategy import generate_signals
from models.backtest import backtest_strategy

def main():
    symbol = 'DMA'
    data = fetch_stock_data(symbol, '2023-01-01', '2023-08-01')
    
    if data is not None:
        print(f"Data fetched for {symbol}:")
        print(data.head())  # Debugging: Check if data is fetched correctly
        
        data = generate_signals(data)
        print("Data after generating signals:")
        print(data.tail())  # Debugging: Check if signals are generated correctly
        
        cumulative_returns = backtest_strategy(data)
        print("Cumulative returns series:")
        print(cumulative_returns.tail())  # Debugging: Check if cumulative returns are calculated correctly

        if not cumulative_returns.empty:
            print(f"Cumulative returns: {cumulative_returns.iloc[-1]:.2f}")
        else:
            print("Cumulative returns is empty, no data to display.")
    else:
        print("Data not available for analysis.")

if __name__ == "__main__":
    main()
