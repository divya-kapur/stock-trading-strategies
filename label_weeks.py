#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 23:15:19 2021

@author: divyakapur
"""

import os
import pandas as pd
input_dir = os.getcwd()
weekly_ticker_file = os.path.join(input_dir, 'K_weekly_return_volatility.csv')
k_weekly = pd.read_csv(weekly_ticker_file)
k_weekly["Label"] = pd.Series(dtype = 'string')

# Loop through the rows and apply labeling rules
for i in range(len(k_weekly) - 1):
    if k_weekly["Closing Price"][i + 1] > k_weekly["Opening Price"][i] and \
       k_weekly["Lowest Price"][i + 1] >= k_weekly["Opening Price"][i] and \
       k_weekly["Closing Price"][i] >= k_weekly["Opening Price"][i]:
        k_weekly.at[i, "Label"] = "Green"
    elif k_weekly["Closing Price"][i + 1] < k_weekly["Opening Price"][i] or \
         k_weekly["Lowest Price"][i + 1] < k_weekly["Opening Price"][i]:
        k_weekly.at[i, "Label"] = "Red"

# Save the labeled data
labeled_filename = os.path.join(input_dir, 'K_weekly_labeled.csv')
k_weekly.to_csv(labeled_filename, index=False)