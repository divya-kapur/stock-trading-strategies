#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 13:28:33 2021

@author: divyakapur
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ticker = 'K'
input_dir = os.getcwd()
weekly_file = os.path.join(input_dir, ticker + '_weekly.csv')
weekly = pd.read_csv(weekly_file)
weekly_detailed_file = os.path.join(input_dir, ticker + '_weekly_detailed.csv')
weekly_detailed = pd.read_csv(weekly_detailed_file)
weekly_detailed
weekly

# Simulate a trading strategy based on weekly 'green' and 'red' labels,
# where 'green' suggests investment and 'red' implies staying in cash.
# Start with $100

weekly_portfolios = []
current_amount = 100
for i, row in weekly.iterrows():
    if i >= len(weekly) - 1:
        break
    weekly_portfolios.append(current_amount)
    if weekly["Label"][i+1] == "Green":
        shares = current_amount / weekly_detailed["Adj Close"][i]
        current_amount = shares * weekly_detailed["Adj Close"][i+1]
    if weekly["Label"][i+1] == "Red":
        if weekly["Label"][i] == "Green":
            shares = current_amount / weekly_detailed["Adj Close"][i]
            current_amount = shares * weekly_detailed["Adj Close"][i]
        elif weekly["Label"][i] == "Red": 
            current_amount = current_amount
weekly_portfolios
plt.plot(weekly_portfolios)

# Compute the average and volatility of weekly balances
year1_portfolios = weekly_portfolios[:52]
year2_portfolios = weekly_portfolios[53:]

year1_mean = sum(year1_portfolios) / len(year1_portfolios)
print("Mean of Year 1:", year1_mean)
year1_volatility = np.std(year1_portfolios)
print("Volatility of Year 1:", year1_volatility)

year2_mean = sum(year2_portfolios) / len(year2_portfolios)
print("Mean of Year 2:", year2_mean)
year2_volatility = np.std(year2_portfolios)
print("Volatility of Year 2:", year2_volatility)

# Plot the growth of our account
plt.plot(year1_portfolios)
plt.plot(year2_portfolios)

# Find the minimum and maximum balances from each year
year1_min = min(year1_portfolios)
year1_min_index = year1_portfolios.index(year1_min)
year1_min_date = weekly_detailed["Date"][year1_min_index]
print("The minimum of year 1 was %.2f on %s " % (year1_min, year1_min_date))

year1_max = max(year1_portfolios)
year1_max_index = year1_portfolios.index(year1_max)
year1_max_date = weekly_detailed["Date"][year1_max_index]
print("The maximum of year 1 was %.2f on %s " % (year1_max, year1_max_date))

year2_min = min(year2_portfolios)
year2_min_index = year2_portfolios.index(year2_min)
year2_min_date = weekly_detailed["Date"][year2_min_index]
print("The minimum of year 2 was %.2f on %s " % (year2_min, year2_min_date))

year2_max = max(year2_portfolios)
year2_max_index = year2_portfolios.index(year2_max)
year2_max_date = weekly_detailed["Date"][year2_max_index]
print("The maximum of year 2 was %.2f on %s " % (year2_max, year2_max_date))

# Compute the final value of the account after each year
year1_final = weekly_portfolios[52]
print("Final Value of Account after Year 1:", year1_final)
year2_final = weekly_portfolios[-1]
print("Final Value of Account after Year 2:", year2_final)

# Compute the maximum # of weeks that our account was growing and 
# what was the maximum # of weeks that our account was 
# decreasing in value each year

weekly_year1 = weekly[weekly["Year"].isin([2019])]
increasing_weeks_year1 = max(weekly_year1[weekly_year1["Label"].isin(["Green"])].groupby((weekly_year1["Label"] != weekly_year1["Label"].shift()).cumsum()).transform("count").agg("Label"))
print("The maximum duration the account was increasing in value in year 1 was %d weeks" % increasing_weeks_year1)

decreasing_weeks_year1 = max(weekly_year1[weekly_year1["Label"].isin(["Red"])].groupby((weekly_year1["Label"] != weekly_year1["Label"].shift()).cumsum()).transform("count").agg("Label"))
print("The maximum duration the account was decreasing in value in year 1 was %d weeks" % decreasing_weeks_year1)

weekly_year2 = weekly[weekly["Year"].isin([2020])]
increasing_weeks_year2 = max(weekly_year2[weekly_year2["Label"].isin(["Green"])].groupby((weekly_year2["Label"] != weekly_year2["Label"].shift()).cumsum()).transform("count").agg("Label"))
print("The maximum duration the account was increasing in value in year 2 was %d weeks" % increasing_weeks_year2)

decreasing_weeks_year2 = max(weekly_year2[weekly_year2["Label"].isin(["Red"])].groupby((weekly_year2["Label"] != weekly_year2["Label"].shift()).cumsum()).transform("count").agg("Label"))
print("The maximum duration the account was decreasing in value in year 2 was %d weeks" % decreasing_weeks_year2)

