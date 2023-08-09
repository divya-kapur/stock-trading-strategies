#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 19:37:45 2021

@author: divyakapur
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
input_dir = os.getcwd()
k_weekly_file = os.path.join(input_dir, 'k_weekly.csv')
k_weekly = pd.read_csv(k_weekly_file)
colors = {'Green':'green', 'Red':'red'}
k_weekly_2019 = k_weekly[k_weekly["Year"].isin([2019])]
fig, ax = plt.subplots()
scatter_2019 = ax.scatter(k_weekly_2019["mean_return"], k_weekly_2019['volatility'], c=k_weekly_2019['Label'].map(colors), s = 5)
for i, row in k_weekly_2019.iterrows():
    ax.annotate(k_weekly_2019["Week_Number"][i], xy = (k_weekly_2019["mean_return"][i], k_weekly_2019["volatility"][i]))
k_weekly_2020 = k_weekly[k_weekly["Year"].isin([2020])]
fig, ax = plt.subplots()
scatter_2020 = ax.scatter(k_weekly_2020["mean_return"], k_weekly_2020['volatility'], c=k_weekly_2020['Label'].map(colors), s = 5)
for i, row in k_weekly_2020.iterrows():
    ax.annotate(k_weekly_2020["Week_Number"][i], xy = (k_weekly_2020["mean_return"][i], k_weekly_2020["volatility"][i]))
