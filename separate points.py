#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 23:05:10 2021

@author: divyakapur
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
input_dir = os.getcwd()
k_weekly_file = os.path.join(input_dir, 'k_weekly.csv')
k_weekly = pd.read_csv(k_weekly_file)
weekly_detailed_file = os.path.join(input_dir, 'k_weekly_detailed.csv')
weekly_detailed = pd.read_csv(weekly_detailed_file)
pd.set_option('mode.chained_assignment', None)

# Construct a reduced dataset by removing some of points such that
# we can draw a line to separate the green points from the red points
# and examine the plots

colors = {'Green':'green', 'Red':'red'}
k_weekly_2019 = k_weekly[k_weekly["Year"].isin([2019])]
k_weekly_2019 = k_weekly_2019.drop(k_weekly_2019[k_weekly_2019["Week_Number"] == 14].index)
k_weekly_2019 = k_weekly_2019.drop(k_weekly_2019[k_weekly_2019["Week_Number"] == 15].index)
k_weekly_2019 = k_weekly_2019.drop(k_weekly_2019[k_weekly_2019["Week_Number"] == 18].index)
k_weekly_2019 = k_weekly_2019.drop(k_weekly_2019[k_weekly_2019["Week_Number"] == 50].index)
k_weekly_2019 = k_weekly_2019.drop(k_weekly_2019[k_weekly_2019["Week_Number"] == 23].index)
k_weekly_2019 = k_weekly_2019.drop(k_weekly_2019[k_weekly_2019["Week_Number"] == 8].index)
k_weekly_2019 = k_weekly_2019.drop(k_weekly_2019[k_weekly_2019["Week_Number"] == 12].index)
k_weekly_2019 = k_weekly_2019.drop(k_weekly_2019[k_weekly_2019["Week_Number"] == 52].index)
k_weekly_2019 = k_weekly_2019.drop(k_weekly_2019[k_weekly_2019["Week_Number"] == 4].index)
k_weekly_2019 = k_weekly_2019.drop(k_weekly_2019[k_weekly_2019["Week_Number"] == 35].index)
k_weekly_2019 = k_weekly_2019.drop(k_weekly_2019[k_weekly_2019["Week_Number"] == 16].index)
k_weekly_2019 = k_weekly_2019.drop(k_weekly_2019[k_weekly_2019["Week_Number"] == 44].index)
k_weekly_2019 = k_weekly_2019.drop(k_weekly_2019[k_weekly_2019["Week_Number"] == 13].index)

k_weekly_2019["volatility"]

fig, ax = plt.subplots()
scatter_2019 = ax.scatter(k_weekly_2019["mean_return"], k_weekly_2019["volatility"], c=k_weekly_2019['Label'].map(colors), s = 5)
for i, row in k_weekly_2019.iterrows():
    ax.annotate(k_weekly_2019["Week_Number"][i], xy = (k_weekly_2019["mean_return"][i], k_weekly_2019["volatility"][i]))

# Manually draw a line to separate the points
# y = 2x + 0.5
# Use this line to assign labels to year 2020

k_weekly_2020 = k_weekly[k_weekly["Year"].isin([2020])]

for i, row in k_weekly_2020.iterrows():
    if (2*(row["mean_return"]) - row["volatility"]) > -0.5:
        k_weekly_2020["Label"][i] = "Green"
    elif (2*(row["mean_return"]) - row["volatility"]) <= -0.5:
        k_weekly_2020["Label"][i] = "Red"
k_weekly_2020

# Simulate a simple trading strategy based on the 'Label' information
# in 2020
weekly = k_weekly_2020
weekly_portfolios = []
current_amount = 100
for i, row in weekly.iterrows():
    if i >= (len(k_weekly) - 1):
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

# Plot the simulated portfolio values over time
plt.plot(weekly_portfolios)
