from downloadData import fetch_stock_data
from plots import plot_trends
from addColumns import add_moving_average, calculate_correlation, StochRSI

#settings
ticker = 'AAPL'
start_date = '2022-01-01'
end_date = '2023-01-01'

#download data from ticker 
stock_data = fetch_stock_data(ticker, start_date, end_date)

#download data from nasdaq
nasdaq_data = fetch_stock_data('^IXIC', start_date, end_date)

#add moving average
stock_data = add_moving_average(stock_data)

#add StochRSI
stock_data = StochRSI(stock_data)

#calculate correlation
correlation = calculate_correlation(stock_data, nasdaq_data)

#show plot trends
plot_trends(stock_data, nasdaq_data, ticker, correlation)

#example of data
#print(stock_data.head())
#print()
#print('\n')
#print(stock_data.tail())