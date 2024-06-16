#moving Average
def add_moving_average(stock_data, window=20):
    stock_data['Moving Average'] = stock_data['Close'].rolling(window=window).mean()
    return stock_data

#correlation
def calculate_correlation(stock_data, index_data):
    correlation = stock_data['Close'].corr(index_data['Close'])
    return correlation

#stochRSI
def StochRSI(stock_data, period=3, column='Close'):
    delta = stock_data[column].diff(1)
    delta.dropna(inplace=True)
    up = delta.copy()
    down = delta.copy()
    up[up<0] = 0
    down[down>0] = 0
    stock_data['up'] = up
    stock_data['down'] = down
    AVG_Gain = stock_data['up'].rolling(window=period).mean()
    AVG_Loss = abs(stock_data['down'].rolling(window=period).mean())
    RS = AVG_Gain / AVG_Loss
    RSI = 100.0 - (100.0 / (1.0 + RS))
    
    stochrsi = (RSI - RSI.rolling(window=period).min()) / (RSI.rolling(window=period).max() - RSI.rolling(window=period).min())
    
    stock_data['StochRSI'] = stochrsi
    
    return stock_data
