#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:15:43 2021

@author: divyakapur
"""

# Add a 'True Label' column
# For each row, i with daily return > 0 = '+', < 0 = '-'
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import os
input_dir = os.getcwd()
ticker_file = os.path.join(input_dir, 'k.csv')
spy_file = os.path.join(input_dir, 'spy.csv')
k = pd.read_csv(ticker_file)
k
spy = pd.read_csv("spy.csv")
spy
k["True Label"] = ["+" if x >= 0 else "-" for x in k["Return"]]
k
spy["True Label"] = ["+" if x >= 0 else "-" for x in spy["Return"]]
spy

# Assuming that all days are independent of each other, and the 
# ratio of 'up' and 'down' days remain the same in the future, 
# take years 1, 2, & 3 and compute the probability that the 
# next day  is an 'up' day.

training_years = [2016, 2017, 2018]
k_training = k[k["Year"].isin(training_years)]
spy_training = spy[spy["Year"].isin(training_years)]
trading_days = len(k_training)
trading_days
# spy_trading_days = len(k[k["Year"].isin(years)])
# spy_trading_days
k_up_days = len(k_training[k_training["True Label"].isin(["+"])])
k_up_days
k_down_days = trading_days - k_up_days
k_down_days
spy_up_days = len(spy_training[spy_training["True Label"].isin(["+"])])
spy_up_days
spy_down_days = trading_days - spy_up_days
spy_down_days
k_up_prob = k_up_days / trading_days
print("The probability of an 'up' day for K:", k_up_prob)
spy_up_prob = spy_up_days / trading_days
print("The probability of an 'up' day for S&P500:", spy_up_prob)

# Take years 1, 2, & 3 and compute the probability that after seeing
# 'k' consecutive 'down' days, the next day is an 'up' day

# k = 1
def one_down_day_prob(dataset):
    plus_counter = 0
    minus_counter = 0 
    for i, row in dataset.iterrows():
        if row["True Label"] == "-":
                i = i + 1
                if i >= len(dataset):
                    break
                next_row = dataset.loc[i]
                if next_row["True Label"] == "+":
                    plus_counter += 1
                else:
                    minus_counter += 1
    prob = plus_counter / (plus_counter + minus_counter)
    return(prob)
print("Probability of an 'up' day after one 'down' day for K : ", one_down_day_prob(k_training))
print("Probability of an 'up' day after one 'down' day for S&P500 : ", one_down_day_prob(spy_training))

# k = 2
def two_down_days_prob(dataset):
    plus_counter = 0
    minus_counter = 0 
    for i, row in dataset.iterrows():
        if row["True Label"] == "-":
                i = i + 1
                if i >= len(dataset):
                    break
                next_row = dataset.loc[i]
                if next_row["True Label"] == "-":
                    i = i + 1
                    if i >= len(dataset):
                        break
                    next_next_row = dataset.loc[i]
                    if next_next_row["True Label"] == "+":
                        plus_counter += 1
                    else:
                        minus_counter += 1
    prob = plus_counter / (plus_counter + minus_counter)
    return(prob)
print("Probability of an 'up' day after two consecutive 'down' days for K : ", two_down_days_prob(k_training))
print("Probability of an 'up' day after two consecutive 'down' days for S&P500 : ", two_down_days_prob(spy_training))

# k = 3
def three_down_days_prob(dataset):
    plus_counter = 0
    minus_counter = 0 
    for i, row in dataset.iterrows():
        if row["True Label"] == "-":
                i = i + 1
                if i >= len(dataset):
                    break
                next_row = dataset.loc[i]
                if next_row["True Label"] == "-":
                    i = i + 1
                    if i >= len(dataset):
                        break
                    next_next_row = dataset.loc[i]
                    if next_next_row["True Label"] == "-":
                        i = i + 1
                        if i >= len(dataset):
                            break
                        next_next_next_row = dataset.loc[i]
                        if next_next_next_row["True Label"] == "+":
                            plus_counter += 1
                        else:
                            minus_counter += 1
    prob = plus_counter / (plus_counter + minus_counter)
    return(prob)
print("Probability of an 'up' day after three consecutive 'down' days for K : ", three_down_days_prob(k_training))
print("Probability of an 'up' day after three consecutive 'down' days for S&P500 : ", three_down_days_prob(spy_training))

# Take years 1, 2, & 3, and compute the probability of seeing an 'up'
# day after 'k' consecutive 'up' days

# k = 1
def one_up_day_prob(dataset):
    plus_counter = 0
    minus_counter = 0 
    for i, row in dataset.iterrows():
        if row["True Label"] == "+":
                i = i + 1
                if i >= len(dataset):
                    break
                next_row = dataset.loc[i]
                if next_row["True Label"] == "+":
                    plus_counter += 1
                else:
                    minus_counter += 1
    prob = plus_counter / (plus_counter + minus_counter)
    return(prob)
print("Probability of another 'up' day after one 'up' day for K : ", one_up_day_prob(k_training))
print("Probability of another 'up' day after one 'up' day for S&P500 : ", one_up_day_prob(spy_training))

# k = 2
def two_up_days_prob(dataset):
    plus_counter = 0
    minus_counter = 0 
    for i, row in dataset.iterrows():
        if row["True Label"] == "+":
                i = i + 1
                if i >= len(dataset):
                    break
                next_row = dataset.loc[i]
                if next_row["True Label"] == "+":
                    i = i + 1
                    if i >= len(dataset):
                        break
                    next_next_row = dataset.loc[i]
                    if next_next_row["True Label"] == "+":
                        plus_counter += 1
                    else:
                        minus_counter += 1
    prob = plus_counter / (plus_counter + minus_counter)
    return(prob)
print("Probability of another 'up' day after two consecutive 'up' days for K : ", two_up_days_prob(k_training))
print("Probability of another 'up' day after two consecutive 'up' days for S&P500 : ", two_up_days_prob(spy_training))

# k = 3
def three_up_days_prob(dataset):
    plus_counter = 0
    minus_counter = 0 
    for i, row in dataset.iterrows():
        if row["True Label"] == "+":
                i = i + 1
                if i >= len(dataset):
                    break
                next_row = dataset.loc[i]
                if next_row["True Label"] == "+":
                    i = i + 1
                    if i >= len(dataset):
                        break
                    next_next_row = dataset.loc[i]
                    if next_next_row["True Label"] == "+":
                        i = i + 1
                        if i >= len(dataset):
                            break
                        next_next_next_row = dataset.loc[i]
                        if next_next_next_row["True Label"] == "+":
                            plus_counter += 1
                        else:
                            minus_counter += 1
    prob = plus_counter / (plus_counter + minus_counter)
    return(prob)
print("Probability of another 'up' day after three consecutive 'up' days for K : ", three_up_days_prob(k_training))
print("Probability of another 'up' day after three consecutive 'up' days for S&P500 : ", three_up_days_prob(spy_training))

# Compute predicted labels for each day in year 4 and 5 based on
# true labels in years 1, 2, & 3 by looking at the pattern of the
# last 'W' labels

testing_years = [2019, 2020]
k_testing = k[k["Year"].isin(testing_years)]
spy_testing = spy[spy["Year"].isin(testing_years)]

# W = 2
def w_2_predicted_labels(dataset, training, testing):
    d_plus1_labels = []
    for i, row in dataset[dataset["Year"].isin([2019,2020])].iterrows():
        pattern = []
        pattern.append(row["True Label"])
        i = i - 1
        d_minus1 = dataset.loc[i]
        pattern.append(d_minus1["True Label"])
        pos_counter = 0
        neg_counter = 0
        for j in range(len(training["True Label"])):
            if j >= (len(training["True Label"]) - 2):
                break
            seq = []        
            seq.append(training["True Label"][j])
            seq.append(training["True Label"][j+1])
            if pattern == seq:
                if training["True Label"][j+2] == "+":
                    pos_counter = pos_counter + 1
                if training["True Label"][j+2] == "-":
                    neg_counter = neg_counter + 1
        if pos_counter > neg_counter:
            d_plus1_labels.append("+")
        elif neg_counter > pos_counter:
            d_plus1_labels.append("-")
    testing["W = 2 Predicted Labels"] = d_plus1_labels
    print(testing)   
w_2_predicted_labels(k, k_training, k_testing)
w_2_predicted_labels(spy, spy_training, spy_testing)

# W = 3
def w_3_predicted_labels(dataset, training, testing):
    d_plus1_labels = []
    for i, row in dataset[dataset["Year"].isin([2019,2020])].iterrows():
        pattern = []
        pattern.append(row["True Label"])
        i = i - 1
        d_minus1 = dataset.loc[i]
        pattern.append(d_minus1["True Label"])
        i = i - 1
        d_minus2 = dataset.loc[i]
        pattern.append(d_minus2["True Label"])
        pos_counter = 0
        neg_counter = 0
        for j in range(len(training["True Label"])):
            if j >= (len(training["True Label"]) - 3):
                break
            seq = []        
            seq.append(training["True Label"][j])
            seq.append(training["True Label"][j+1])
            seq.append(training["True Label"][j+2])
            if pattern == seq:
                if training["True Label"][j+3] == "+":
                    pos_counter = pos_counter + 1
                if training["True Label"][j+3] == "-":
                    neg_counter = neg_counter + 1
        if pos_counter > neg_counter:
            d_plus1_labels.append("+")
        elif neg_counter > pos_counter:
            d_plus1_labels.append("-")
    testing["W = 3 Predicted Labels"] = d_plus1_labels
    print(testing)   
w_3_predicted_labels(k, k_training, k_testing)
w_3_predicted_labels(spy, spy_training, spy_testing)

# W = 4
def w_4_predicted_labels(dataset, training, testing):
    d_plus1_labels = []
    for i, row in dataset[dataset["Year"].isin([2019,2020])].iterrows():
        pattern = []
        pattern.append(row["True Label"])
        i = i - 1
        d_minus1 = dataset.loc[i]
        pattern.append(d_minus1["True Label"])
        i = i - 1
        d_minus2 = dataset.loc[i]
        pattern.append(d_minus2["True Label"])
        i = i - 1
        d_minus3 = dataset.loc[i]
        pattern.append(d_minus3["True Label"])
        pos_counter = 0
        neg_counter = 0
        for j in range(len(training["True Label"])):
            if j >= (len(training["True Label"]) - 4):
                break
            seq = []        
            seq.append(training["True Label"][j])
            seq.append(training["True Label"][j+1])
            seq.append(training["True Label"][j+2])
            seq.append(training["True Label"][j+3])
            if pattern == seq:
                if training["True Label"][j+4] == "+":
                    pos_counter = pos_counter + 1
                if training["True Label"][j+4] == "-":
                    neg_counter = neg_counter + 1
        if pos_counter > neg_counter:
            d_plus1_labels.append("+")
        elif neg_counter > pos_counter:
            d_plus1_labels.append("-")
        elif pos_counter == neg_counter:
            d_plus1_labels.append("+")
    testing["W = 4 Predicted Labels"] = d_plus1_labels
    print(testing)   
w_4_predicted_labels(k, k_training, k_testing)
w_4_predicted_labels(spy, spy_training, spy_testing)

# For each W, compute the accuracy (i.e. what percentage of true labels
# you have predicted correctly for the last two years)

# W = 2 Accuracy
def w_2_accuracy(dataset, testing):
    correct = 0
    pos_correct = 0
    neg_correct = 0
    incorrect = 0
    for i, row in testing.iterrows():
        if i >= (len(dataset) - 1):
            break
        if row["W = 2 Predicted Labels"] == testing["True Label"][i+1]:
            correct = correct + 1
            if row["W = 2 Predicted Labels"] == "+":
                pos_correct = pos_correct + 1
            else:
                neg_correct = neg_correct + 1
        else:
            incorrect = incorrect + 1
    total_accuracy = (correct / ((pos_correct + neg_correct) + incorrect)) * 100
    pos_accuracy = (pos_correct / ((pos_correct + neg_correct) + incorrect)) * 100
    neg_accuracy = (neg_correct / ((pos_correct + neg_correct) + incorrect)) * 100
    return([total_accuracy, pos_accuracy, neg_accuracy])
print("Accuracy of the W = 2 Labels for K (total, +, -):", w_2_accuracy(k, k_testing))
print("Accuracy of the W = 2 Labels for S&P500 (total, +, -):", w_2_accuracy(spy, spy_testing))

# W = 3 Accuracy
def w_3_accuracy(dataset, testing):
    correct = 0
    pos_correct = 0
    neg_correct = 0
    incorrect = 0
    for i, row in testing.iterrows():
        if i >= (len(dataset) - 1):
            break
        if row["W = 3 Predicted Labels"] == testing["True Label"][i+1]:
            correct = correct + 1
            if row["W = 3 Predicted Labels"] == "+":
                pos_correct = pos_correct + 1
            else:
                neg_correct = neg_correct + 1
        else:
            incorrect = incorrect + 1
    total_accuracy = (correct / ((pos_correct + neg_correct) + incorrect)) * 100
    pos_accuracy = (pos_correct / ((pos_correct + neg_correct) + incorrect)) * 100
    neg_accuracy = (neg_correct / ((pos_correct + neg_correct) + incorrect)) * 100
    return([total_accuracy, pos_accuracy, neg_accuracy])
print("Accuracy of the W = 3 Labels for K (total, +, -):", w_3_accuracy(k, k_testing))
print("Accuracy of the W = 3 Labels for S&P500 (total, +, -):", w_3_accuracy(spy, spy_testing))

# W = 4 Accuracy
def w_4_accuracy(dataset, testing):
    correct = 0
    pos_correct = 0
    neg_correct = 0
    incorrect = 0
    for i, row in testing.iterrows():
        if i >= (len(dataset) - 1):
            break
        if row["W = 4 Predicted Labels"] == testing["True Label"][i+1]:
            correct = correct + 1
            if row["W = 4 Predicted Labels"] == "+":
                pos_correct = pos_correct + 1
            else:
                neg_correct = neg_correct + 1
        else:
            incorrect = incorrect + 1
    total_accuracy = (correct / ((pos_correct + neg_correct) + incorrect)) * 100
    pos_accuracy = (pos_correct / ((pos_correct + neg_correct) + incorrect)) * 100
    neg_accuracy = (neg_correct / ((pos_correct + neg_correct) + incorrect)) * 100
    return([total_accuracy, pos_accuracy, neg_accuracy])
print("Accuracy of the W = 4 Labels for K (total, +, -):", w_4_accuracy(k, k_testing))
print("Accuracy of the W = 4 Labels for S&P500 (total, +, -):", w_4_accuracy(spy, spy_testing))

# W = 2 gave the highest accuracy for K and W = 2/W = 3 gave the highest accuracy for S&P500

# Using the preducted labels for W = 2, W = 3, & W = 4, use ensemble
# learning to combine predictions to compute ensemble labels

def ensemble_labels(testing):
    ensemble_labels = []
    plus_counter = 0
    minus_counter = 0
    for i, row in testing.iterrows():
        if row["W = 2 Predicted Labels"] == "+":
            plus_counter = plus_counter + 1
        elif row["W = 2 Predicted Labels"] == "-":
            minus_counter = minus_counter + 1
        if row["W = 3 Predicted Labels"] == "+":
            plus_counter = plus_counter + 1
        elif row["W = 3 Predicted Labels"] == "-":
            minus_counter = minus_counter + 1 
        if row["W = 4 Predicted Labels"] == "+":
            plus_counter = plus_counter + 1 
        elif row["W = 4 Predicted Labels"] == "-":
            minus_counter = minus_counter + 1
        if plus_counter > minus_counter:
            ensemble_labels.append("+")
        else:
            ensemble_labels.append("-")
    testing["Ensemble Labels"] = ensemble_labels
    print(testing)
ensemble_labels(k_testing)
ensemble_labels(spy_testing)

# Compute how many labels in year 4 and 5 are correctly computed 
# using ensemble learning
def ensemble_accuracy(dataset, testing):
    correct = 0
    pos_correct = 0
    neg_correct = 0
    incorrect = 0
    for i, row in testing.iterrows():
        if i >= (len(dataset) - 1):
            break
        if row["Ensemble Labels"] == testing["True Label"][i+1]:
            correct = correct + 1
            if row["Ensemble Labels"] == "+":
                pos_correct = pos_correct + 1
            elif row["Ensemble Labels"] == "-":
                neg_correct = neg_correct + 1
        elif row["Ensemble Labels"] != testing["True Label"][i+1]:
            incorrect = incorrect + 1
    total_accuracy = (correct / ((pos_correct + neg_correct) + incorrect)) * 100
    pos_accuracy = (pos_correct / ((pos_correct + neg_correct) + incorrect)) * 100
    neg_accuracy = (neg_correct / ((pos_correct + neg_correct) + incorrect)) * 100
    return([total_accuracy, pos_accuracy, neg_accuracy])
print("Accuracy of total Ensemble Labels for K:", ensemble_accuracy(k, k_testing)[0])
print("Accuracy of total Ensemble Labels for S&P500 :", ensemble_accuracy(spy, spy_testing)[0])

# Accuracy of predicting '-' labels by using ensemble compared to W = 2,3,4
print("Accuracy of W = 2 Labels for K:", w_2_accuracy(k, k_testing)[2])
print("Accuracy of W = 3 Labels for K:", w_3_accuracy(k, k_testing)[2])
print("Accuracy of W = 4 Labels for K:", w_4_accuracy(k, k_testing)[2])
print("Accuracy of Negative Ensemble Labels for K:", ensemble_accuracy(k, k_testing)[2])

print("Accuracy of W = 2 Labels for S&P500:", w_2_accuracy(spy, spy_testing)[2])
print("Accuracy of W = 3 Labels for S&P500:", w_3_accuracy(spy, spy_testing)[2])
print("Accuracy of W = 4 Labels for S&P500:", w_4_accuracy(spy, spy_testing)[2])
print("Accuracy of Negative Ensemble Labels for S&P500:", ensemble_accuracy(spy, spy_testing)[2])

# The accuracy of predicting '-' labels did not improve using ensemble

# Accuracy of predicting '+' labels by using ensemble compared to W = 2,3,4

print("Accuracy of W = 2 Labels for K:", w_2_accuracy(k, k_testing)[1])
print("Accuracy of W = 3 Labels for K:", w_3_accuracy(k, k_testing)[1])
print("Accuracy of W = 4 Labels for K:", w_4_accuracy(k, k_testing)[1])
print("Accuracy of Negative Ensemble Labels for K:", ensemble_accuracy(k, k_testing)[1])

print("Accuracy of W = 2 Labels for S&P500:", w_2_accuracy(spy, spy_testing)[1])
print("Accuracy of W = 3 Labels for S&P500:", w_3_accuracy(spy, spy_testing)[1])
print("Accuracy of W = 4 Labels for S&P500:", w_4_accuracy(spy, spy_testing)[1])
print("Accuracy of Negative Ensemble Labels for S&P500:", ensemble_accuracy(spy, spy_testing)[1])

# The accuracy of predicting '+' labels did improve using ensemble

# For W = 2,3,4 and ensemble, compute performance statistics

# W = 2 Stats
def w_2_stats(dataset, testing):
    tp = 0
    tn = 0 
    fp = 0
    fn = 0
    for i, row in testing.iterrows():
        if i >= (len(dataset) - 1):
            break
        if row["W = 2 Predicted Labels"] == testing["True Label"][i+1]:
            if row["W = 2 Predicted Labels"] == ("+"):
                tp = tp + 1
            elif row["W = 2 Predicted Labels"] == ("-"):
                tn = tn + 1
        elif row["W = 2 Predicted Labels"] != testing["True Label"][i+1]:
            if row["W = 2 Predicted Labels"] == ("+"):
                fp = fp + 1
            elif row["W = 2 Predicted Labels"] == ("-"):
                fn = fn + 1
    tpr = tp / (tp + fn)
    tnr = tn / (tn + fp)
    return([tp, tn, fp, fn, tpr, tnr])
print("TP for W = 2 (K):", w_2_stats(k, k_testing)[0])
print("FP for W = 2 (K):", w_2_stats(k, k_testing)[2])
print("TN for W = 2 (K):", w_2_stats(k, k_testing)[1])
print("FN for W = 2 (K):", w_2_stats(k, k_testing)[3])
print("Accuracy for W = 2 (K):", w_2_accuracy(k, k_testing)[0])
print("TPR for W = 2 (K):", w_2_stats(k, k_testing)[4])
print("TNR for W = 2 (K):", w_2_stats(k, k_testing)[5])

print("TP for W = 2 (S&P500):", w_2_stats(spy, spy_testing)[0])
print("FP for W = 2 (S&P500):", w_2_stats(spy, spy_testing)[2])
print("TN for W = 2 (S&P500):", w_2_stats(spy, spy_testing)[1])
print("FN for W = 2 (S&P500):", w_2_stats(spy, spy_testing)[3])
print("Accuracy for W = 2 (S&P500):", w_2_accuracy(spy, spy_testing)[0])
print("TPR for W = 2 (S&P500):", w_2_stats(spy, spy_testing)[4])
print("TNR for W = 2 (S&P500):", w_2_stats(spy, spy_testing)[5])

# W = 3 Stats
def w_3_stats(dataset, testing):
    tp = 0
    tn = 0 
    fp = 0
    fn = 0
    for i, row in testing.iterrows():
        if i >= (len(dataset) - 1):
            break
        if row["W = 3 Predicted Labels"] == testing["True Label"][i+1]:
            if row["W = 3 Predicted Labels"] == ("+"):
                tp = tp + 1
            elif row["W = 3 Predicted Labels"] == ("-"):
                tn = tn + 1
        elif row["W = 3 Predicted Labels"] != testing["True Label"][i+1]:
            if row["W = 3 Predicted Labels"] == ("+"):
                fp = fp + 1
            elif row["W = 3 Predicted Labels"] == ("-"):
                fn = fn + 1
    tpr = tp / (tp + fn)
    tnr = tn / (tn + fp)
    return([tp, tn, fp, fn, tpr, tnr])
print("TP for W = 3 (K):", w_3_stats(k, k_testing)[0])
print("FP for W = 3 (K):", w_3_stats(k, k_testing)[2])
print("TN for W = 3 (K):", w_3_stats(k, k_testing)[1])
print("FN for W = 3 (K):", w_3_stats(k, k_testing)[3])
print("Accuracy for W = 3 (K):", w_3_accuracy(k, k_testing)[0])
print("TPR for W = 3 (K):", w_3_stats(k, k_testing)[4])
print("TNR for W = 3 (K):", w_3_stats(k, k_testing)[5])

print("TP for W = 3 (S&P500):", w_3_stats(spy, spy_testing)[0])
print("FP for W = 3 (S&P500):", w_3_stats(spy, spy_testing)[2])
print("TN for W = 3 (S&P500):", w_3_stats(spy, spy_testing)[1])
print("FN for W = 3 (S&P500):", w_3_stats(spy, spy_testing)[3])
print("Accuracy for W = 3 (S&P500):", w_3_accuracy(spy, spy_testing)[0])
print("TPR for W = 3 (S&P500):", w_3_stats(spy, spy_testing)[4])
print("TNR for W = 3 (S&P500):", w_3_stats(spy, spy_testing)[5])

# W = 4 Stats
def w_4_stats(dataset, testing):
    tp = 0
    tn = 0 
    fp = 0
    fn = 0
    for i, row in testing.iterrows():
        if i >= (len(dataset) - 1):
            break
        if row["W = 4 Predicted Labels"] == testing["True Label"][i+1]:
            if row["W = 4 Predicted Labels"] == ("+"):
                tp = tp + 1
            elif row["W = 4 Predicted Labels"] == ("-"):
                tn = tn + 1
        elif row["W = 4 Predicted Labels"] != testing["True Label"][i+1]:
            if row["W = 4 Predicted Labels"] == ("+"):
                fp = fp + 1
            elif row["W = 4 Predicted Labels"] == ("-"):
                fn = fn + 1
    tpr = tp / (tp + fn)
    tnr = tn / (tn + fp)
    return([tp, tn, fp, fn, tpr, tnr])
print("TP for W = 4 (K):", w_4_stats(k, k_testing)[0])
print("FP for W = 4 (K):", w_4_stats(k, k_testing)[2])
print("TN for W = 4 (K):", w_4_stats(k, k_testing)[1])
print("FN for W = 4 (K):", w_4_stats(k, k_testing)[3])
print("Accuracy for W = 4 (K):", w_4_accuracy(k, k_testing)[0])
print("TPR for W = 4 (K):", w_4_stats(k, k_testing)[4])
print("TNR for W = 4 (K):", w_4_stats(k, k_testing)[5])

print("TP for W = 4 (S&P500):", w_4_stats(spy, spy_testing)[0])
print("FP for W = 4 (S&P500):", w_4_stats(spy, spy_testing)[2])
print("TN for W = 4 (S&P500):", w_4_stats(spy, spy_testing)[1])
print("FN for W = 4 (S&P500):", w_4_stats(spy, spy_testing)[3])
print("Accuracy for W = 4 (S&P500):", w_4_accuracy(spy, spy_testing)[0])
print("TPR for W = 4 (S&P500):", w_4_stats(spy, spy_testing)[4])
print("TNR for W = 4 (S&P500):", w_4_stats(spy, spy_testing)[5])

# Ensemble Stats
def ensemble_stats(dataset, testing):
    tp = 0
    tn = 0 
    fp = 0
    fn = 0
    for i, row in testing.iterrows():
        if i >= (len(dataset) - 1):
            break
        if row["Ensemble Labels"] == testing["True Label"][i+1]:
            if row["Ensemble Labels"] == ("+"):
                tp = tp + 1
            elif row["Ensemble Labels"] == ("-"):
                tn = tn + 1
        elif row["Ensemble Labels"] != testing["True Label"][i+1]:
            if row["Ensemble Labels"] == ("+"):
                fp = fp + 1
            elif row["Ensemble Labels"] == ("-"):
                fn = fn + 1
    tpr = tp / (tp + fn)
    tnr = tn / (tn + fp)
    return([tp, tn, fp, fn, tpr, tnr])
print("TP for Ensemble (K):", ensemble_stats(k, k_testing)[0])
print("FP for Ensemble (K):", ensemble_stats(k, k_testing)[2])
print("TN for Ensemble (K):", ensemble_stats(k, k_testing)[1])
print("FN for Ensemble (K):", ensemble_stats(k, k_testing)[3])
print("Accuracy for Ensemble (K):", ensemble_accuracy(k, k_testing)[0])
print("TPR for Ensemble (K):", ensemble_stats(k, k_testing)[4])
print("TNR for Ensemble (K):", ensemble_stats(k, k_testing)[5])

print("TP for Ensemble (S&P500):", ensemble_stats(spy, spy_testing)[0])
print("FP for Ensemble (S&P500):", ensemble_stats(spy, spy_testing)[2])
print("TN for Ensemble (S&P500):", ensemble_stats(spy, spy_testing)[1])
print("FN for Ensemble (S&P500):", ensemble_stats(spy, spy_testing)[3])
print("Accuracy for Ensemble (S&P500):", ensemble_accuracy(spy, spy_testing)[0])
print("TPR for Ensemble (S&P500):", ensemble_stats(spy, spy_testing)[4])
print("TNR for Ensemble (S&P500):", ensemble_stats(spy, spy_testing)[5])

spy_testing[["W = 2 Predicted Labels", "Ensemble Labels"]]
