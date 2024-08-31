import pandas as pd

def moving_average(df, window):
    return df['Close'].rolling(window=window).mean()

def relative_strength_index(df, period=14):
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def bollinger_bands(df, window=20, num_std_dev=2):
    ma = moving_average(df, window)
    std_dev = df['Close'].rolling(window=window).std()
    upper_band = ma + (std_dev * num_std_dev)
    lower_band = ma - (std_dev * num_std_dev)
    return upper_band, lower_band

def macd(df, short_period=12, long_period=26, signal_period=9):
    short_ema = df['Close'].ewm(span=short_period, adjust=False).mean()
    long_ema = df['Close'].ewm(span=long_period, adjust=False).mean()
    macd_line = short_ema - long_ema
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
    return macd_line, signal_line

def average_true_range(df, period=14):
    high_low = df['High'] - df['Low']
    high_close = (df['High'] - df['Close'].shift()).abs()
    low_close = (df['Low'] - df['Close'].shift()).abs()
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    atr = tr.rolling(window=period).mean()
    return atr
