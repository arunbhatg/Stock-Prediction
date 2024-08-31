def backtest_strategy(df):
    df['Position'] = df['Buy'].shift(1).fillna(False).astype(int)
    df['Strategy_Returns'] = df['Position'] * df['Close'].pct_change()
    cumulative_returns = (1 + df['Strategy_Returns']).cumprod() - 1
    return cumulative_returns
