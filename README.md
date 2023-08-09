# stock-trading-stratgies
Implemented machine learning classifiers to predict 'green' or 'red' investment weeks based on attributes like mean and standard deviation of daily returns, comparing various stategies for portfolio growth

To generate stock data:

  1. Choose a stock ticker (I used K & SPY)
  2. Use the script _read_and_save_stock_data.py_ to download daily stock data (5-years from Jan 1, 2014 to Dec 31, 2019) for your ticker as a CSV file (using Pandas Yahoo stock market reader). In this script, you would need to change the ticker to the name that you have chosen in Task 1. This script downloads historical data and computes additional fields for time (week, day, month) and prices (daily returns, 14- and 50-day moving price averages).
  3. Use the script _read_stock_data_from_file.py_ to read your saved CSV file into a list of lines.

Scripts : 
  * **predicting_daily_trading_labels.py**: for predicting daily trading labels using ensemble learning and analyzing prediction accuracy and portfolio growth based on different patterns
  * **trading_strategies.py**: simulates different investment strategies
  * **stock data plot.py**: displays and saves a plot of prices between two dates
