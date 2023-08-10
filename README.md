# stock-trading-stratgies
Implemented machine learning classifiers to predict 'green' or 'red' investment weeks based on attributes like mean and standard deviation of daily returns, comparing various stategies for portfolio growth

To generate stock data:

  1. Choose a stock ticker (I used K & SPY)
  2. Use the script _read_and_save_stock_data.py_ to download daily stock data (5-years from Jan 1, 2014 to Dec 31, 2019) for your ticker as a CSV file (using Pandas Yahoo stock market reader). In this script, you would need to change the ticker to the name that you have chosen in Task 1. This script downloads historical data and computes additional fields for time (week, day, month) and prices (daily returns, 14- and 50-day moving price averages).
  3. Use the script _read_stock_data_from_file.py_ to read your saved CSV file into a list of lines.

Scripts : 
  * **predicting_daily_trading_labels.py**: for predicting daily trading labels using ensemble learning and analyzing prediction accuracy and portfolio growth based on different patterns
  * **trading_strategies.py**: simulates different investment strategies
  * **stock_data_plot.py**: displays and saves a plot of prices between two dates
  * **label_weeks.py**: automates the process of labelling weekly stock data as "green" or "red". The script assigns "green" labels to weeks when the closing price at the end of the week is higher than the opening price without significant price volatility, and "red" label to weeks when the closing price is lower than the opening price or experiences dips below the opening price during the week.
  * **compute_stocks_weekly_return_volatility.py**: retrieves historical stock price data and calculates weekly returns and their statistics (mean and volatility) for each year and week, and generates two CSV files: one with summarized statistics and another that combines these statistics with the original data. The data is gathered between January 2019 and December 2020
  * **examine_labels.py**: generates scatter plots using Matplotlib to visualize the correlation between mean returns, volatility, and color labels ("Green" or "Red") assigned to stock data for the years 2019 and 2020
  * **trading_with_labels.py**: simulates a trading strategy for a stock using weekly "green" and "red" labels, starting with $100. It calculates account growth, volatility, and analyzes the duration of value increase and decrease for each year.
  * 
