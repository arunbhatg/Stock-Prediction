from .technical_indicators import moving_average, relative_strength_index, bollinger_bands, macd, average_true_range

def generate_signals(df):
    df['MA50'] = moving_average(df, 50)
    df['MA200'] = moving_average(df, 200)
    df['RSI'] = relative_strength_index(df)
    df['Upper_Band'], df['Lower_Band'] = bollinger_bands(df)
    df['MACD_Line'], df['Signal_Line'] = macd(df)
    df['ATR'] = average_true_range(df)

    # Complex Strategy Example:
    # Buy when:
    # - RSI is below 30 (oversold)
    # - Close price crosses above the lower Bollinger Band
    # - MACD line crosses above the signal line (bullish crossover)
    # - Price is above the 200-day moving average (indicating an uptrend)

    df['Buy'] = (
        (df['RSI'] < 30) &
        (df['Close'] > df['Lower_Band']) &
        (df['MACD_Line'] > df['Signal_Line']) &
        (df['Close'] > df['MA200'])
    )

    # Sell when:
    # - RSI is above 70 (overbought)
    # - Close price crosses below the upper Bollinger Band
    # - MACD line crosses below the signal line (bearish crossover)
    # - Price is below the 50-day moving average (indicating a downtrend)

    df['Sell'] = (
        (df['RSI'] > 70) &
        (df['Close'] < df['Upper_Band']) &
        (df['MACD_Line'] < df['Signal_Line']) &
        (df['Close'] < df['MA50'])
    )

    return df
