#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:54:58 2021

@author: divyakapur
"""
import pandas as pd
import numpy as np
import os

input_dir = os.getcwd()
ticker_file = os.path.join(input_dir, 'k.csv')
spy_file = os.path.join(input_dir, 'spy.csv')
k = pd.read_csv(ticker_file)
spy = pd.read_csv(spy_file)

# Calculate the mean and standard deviation of daily returns
# for each weekday for each year from 2016 to 2020

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
years = [2016, 2017, 2018, 2019, 2020]

def calc_stats(data, year_range):
    results = {}

    for year in year_range:
        year_data = data[data["Year"].isin([year])]
        year_returns = {weekday: [] for weekday in weekdays}

        for _, row in year_data.iterrows():
            weekday = row["Weekday"]
            year_returns[weekday].append(row["Return"])

        for weekday, returns in year_returns.items():
            mean_return = np.mean(returns) * 100
            sd_return = np.std(returns)
            results[f"Mean of {year} {weekday}s"] = mean_return
            results[f"SD of {year} {weekday}s"] = sd_return
    return results

year_range = range(2016, 2021)
k_results = calc_stats(k, year_range)
spy_results = calc_stats(spy, year_range)

for key, value in k_results.items():
    print(key + ':', value)

for key, value in spy_results.items():
    print(key + ':', value)


# Compute the mean and SD of each +/- weekday for each year

def mean_sd(data):
    mean = sum(data) / len(data)
    var = sum((x-mean)**2 for x in data) / len(data)
    sd = var ** 0.5
    return mean, sd

def weekday_mean_sd(data):
    for weekday in weekdays:
        for year in years:
            positive_returns = data[(data["Weekday"] == weekday) & (data["Year"] == year) & (data["Return"] >= 0)]["Return"]
            negative_returns = data[(data["Weekday"] == weekday) & (data["Year"] == year) & (data["Return"] < 0)]["Return"]

            if len(positive_returns) > 0:
                mean_positive, sd_positive = mean_sd(positive_returns)
                print(f"Mean of Positive {weekday}s in {year}: {mean_positive}")
                print(f"SD of Positive {weekday}s in {year}: {sd_positive}")
                print(f"Number of Positive {weekday}s in {year}: {len(positive_returns)}")

            if len(negative_returns) > 0:
                mean_negative, sd_negative = mean_sd(negative_returns)
                print(f"Mean of Negative {weekday}s in {year}: {mean_negative}")
                print(f"SD of Negative {weekday}s in {year}: {sd_negative}")
                print(f"Number of Negative {weekday}s in {year}: {len(negative_returns)}")

weekday_mean_sd(k)
weekday_mean_sd(spy)

# Use an 'oracle' to predict the investment amount if we reinvest
# the gained amount back to compound our gains. Start with $100.
k_final_money_oracle = 100
for i,row in k.iterrows():
    if row["Return"] >= 0:
        k_final_money_oracle = k_final_money_oracle * (1 + row["Return"])
print("Amount of Money for year 5 of K:", k_final_money_oracle)
        
spy_final_money_oracle = 100
for i,row in spy.iterrows():
    if row["Return"] >= 0:
        spy_final_money_oracle = spy_final_money_oracle * (1 + row["Return"])
print("Amount of Money for year 5 of SPY:", spy_final_money_oracle)

# Simulate 'buy and hold' stategy by seeing what an initial investment
# of $100 would have returned if we simply held the stocks without selling
k_final_money_buy_and_hold = 100
for i,row in k.iterrows():
        k_final_money_buy_and_hold = k_final_money_buy_and_hold * (1 + row["Return"])
print("Amount of Money for year 5 of K:", k_final_money_buy_and_hold)

spy_final_money_buy_and_hold = 100
for i,row in spy.iterrows():
        spy_final_money_buy_and_hold = spy_final_money_buy_and_hold * (1 + row["Return"])
print("Amount of Money for year 5 of SPY:", spy_final_money_buy_and_hold)


# Simulate a scenario where we take 'revenge' on the top 10 worst-performing 
# days. Assume that after the 10 bad days, the stock will start performing
# positively starting with $100. 
k_final_money_oracle_revenge_a = 100
for i, row in k.sort_values(by = "Return",ascending = False)[10:].iterrows():
    if row["Return"] >= 0:
        k_final_money_oracle_revenge_a = k_final_money_oracle_revenge_a * (1 + row["Return"])
print("Amount of Money for year 5 of K: ", k_final_money_oracle_revenge_a)

spy_final_money_oracle_revenge_a = 100
for i, row in spy.sort_values(by = "Return",ascending = False)[10:].iterrows():
    if row["Return"] >= 0:
        spy_final_money_oracle_revenge_a = spy_final_money_oracle_revenge_a * (1 + row["Return"])
print("Amount of Money for year 5 of SPY: ", spy_final_money_oracle_revenge_a)

# Take 'revenge' on the top 10-best performing days -- assume that 
# after 10 great days the stock will start performing negatively
k_final_money_oracle_revenge_b = 100
for i, row in k.sort_values(by = "Return",ascending = False)[:(len(k)-10)].iterrows():
    if row["Return"] >= 0:
        k_final_money_oracle_revenge_b = k_final_money_oracle_revenge_b * (1 + row["Return"])
print("Amount of Money for year 5 of K: ", k_final_money_oracle_revenge_b)

spy_final_money_oracle_revenge_b = 100
for i, row in spy.sort_values(by = "Return",ascending = False)[:(len(spy)-11)].iterrows():
    if row["Return"] >= 0:
        spy_final_money_oracle_revenge_b = spy_final_money_oracle_revenge_b * (1 + row["Return"])
print("Amount of Money for year 5 of SPY: ", spy_final_money_oracle_revenge_b)
    
# Take 'revenge' on the 5 days with the highest + returns as well as the
# 5 days with the highest - returns -- assume that after these 10
# extreme days, the stock's performance will change
k_final_money_oracle_revenge_c = 100
for i, row in k.sort_values(by = "Return",ascending = False)[5:(len(k)-6)].iterrows():
    if row["Return"] >= 0:
        k_final_money_oracle_revenge_c = k_final_money_oracle_revenge_c * (1 + row["Return"])
print("Amount of Money for year 5 of K: ", k_final_money_oracle_revenge_c)

spy_final_money_oracle_revenge_c = 100
for i, row in spy.sort_values(by = "Return",ascending = False)[5:(len(spy)-6)].iterrows():
    if row["Return"] >= 0:
        spy_final_money_oracle_revenge_c = spy_final_money_oracle_revenge_c * (1 + row["Return"])
print("Amount of Money for year 5 of SPY: ", spy_final_money_oracle_revenge_c)
