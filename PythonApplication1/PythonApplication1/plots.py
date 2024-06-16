import matplotlib.pyplot as plt
import mplcursors
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator

#plot trends
def plot_trends(stock_data, nasdaq_data, ticker, correlation):
    num_ticks = 10
    num_minor_ticks = 5
    plt.figure(figsize=(14, 10))
    plt.ioff()
    
    ax1 = plt.subplot(4, 1, 1)
    ax1.plot(stock_data['Close'], label='Close Price', color='blue')
    ax1.plot(stock_data['Moving Average'], label='Moving Average', color='orange', linestyle='dotted')
    max_price = stock_data['Close'].max()
    min_price = stock_data['Close'].min()
    ax1.axhline(max_price, color='green', linestyle='--')
    ax1.axhline(min_price, color='red', linestyle='--')
    ax1.text(stock_data.index[0], max_price, ' Max: $'+str(max_price), verticalalignment='bottom', color='green')
    ax1.text(stock_data.index[0], min_price, ' Min: $'+str(min_price), verticalalignment='bottom', color='red')
    ax1.set_title(ticker + ' Close Price Trend with Moving Average')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price ($)')
    ax1.legend()
    
    ax1.xaxis.set_major_locator(MaxNLocator(num_ticks))
    ax1.yaxis.set_major_locator(MaxNLocator(num_ticks))
    ax1.xaxis.set_minor_locator(MaxNLocator(num_minor_ticks))
    ax1.yaxis.set_minor_locator(MaxNLocator(num_minor_ticks))
    ax1.grid(which='major', color='#CCCCCC', linestyle='--')
    ax1.grid(which='minor', color='#CCCCCC', linestyle=':')

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_minor_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=0)
    plt.setp(ax1.xaxis.get_minorticklabels(), rotation=0)
    
    ax2 = plt.subplot(4, 1, 3, sharex=ax1)
    ax2.bar(stock_data.index, stock_data['Volume'], color='green', alpha=0.3)
    ax2.set_title('Volume Trend')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Daily Volume ($)')
    ax2.grid()

    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax2.xaxis.set_minor_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=0)
    plt.setp(ax2.xaxis.get_minorticklabels(), rotation=0)

    ax3 = plt.subplot(4, 1, 4, sharex=ax1)
    ax3.plot(stock_data['StochRSI'], label='StochRSI', color='purple')
    ax3.axhline(0.8, color='red', linestyle='--')
    ax3.axhline(0.2, color='green', linestyle='--')
    ax3.set_title('Stochastic RSI')
    ax3.set_xlabel('Date')
    ax3.set_ylabel('StochRSI')
    ax3.legend()
    ax3.grid()
    
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax3.xaxis.set_minor_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.setp(ax3.xaxis.get_majorticklabels(), rotation=0)
    plt.setp(ax3.xaxis.get_minorticklabels(), rotation=0)
    
    ax4 = plt.subplot(4, 1, 2)
    ax4.plot(nasdaq_data['Close'], label='Close Price', color='purple')
    ax4.set_title('NASDAQ Composite Close Price')
    ax4.set_xlabel('Date')
    ax4.set_ylabel('Price ($)')
    ax4.legend()
    ax4.xaxis.set_major_locator(MaxNLocator(num_ticks))
    ax4.yaxis.set_major_locator(MaxNLocator(num_ticks))
    ax4.xaxis.set_minor_locator(MaxNLocator(num_minor_ticks))
    ax4.yaxis.set_minor_locator(MaxNLocator(num_minor_ticks))
    ax4.grid(which='major', color='#CCCCCC', linestyle='--')
    ax4.grid(which='minor', color='#CCCCCC', linestyle=':')
    
    ax4.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax4.xaxis.set_minor_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.setp(ax4.xaxis.get_majorticklabels(), rotation=0)
    plt.setp(ax4.xaxis.get_minorticklabels(), rotation=0)
    
    plt.figtext(0.5, 0.001, f'Correlation between {ticker} stock closing and NASDAQ index: {correlation:.2f}', fontsize=12, ha='center')
    
    mplcursors.cursor(hover=True)

    plt.tight_layout()
    plt.show()