
"""
Box plot main use is 
to find outliers in the data, to find the distribution of the data, to find the median of the data, to find the interquartile range of the data, to find the minimum and maximum of the data, to find the mean of the data, to find the standard deviation of the data, to find the variance of the data, to find the skewness of the data, to find the kurtosis of the data, to find the range of the data, to find the coefficient of variation of the data, to find the z-score of the data, to find the percentile of the data, to find the quartiles of the data, to find the deciles of the data, to find the mode of the data, to find the median absolute deviation of the data, to find the interquartile range of the data, to find the outliers in the data, to find the distribution of the data, to find the mean absolute deviation of the data, to find the standard error of mean of the data, to find confidence interval of mean of the data

25th percentile = Q1
50th percentile = Q2 = median
75th percentile = Q3
minimum = Q1 - 1.5 * IQR
maximum = Q3 + 1.5 * IQR
iqr = Q3 - Q1
whiskers = 1.5 * IQR

here outliers are shown as points outside the whiskers,
for right skwed distribution, the whiskers will be longer on the right side, for left skewed distribution,
 the whiskers will be longer on the left side, for normal distribution, the whiskers will be of equal length on both sides


"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

path = r'Numpy\handlingmissingvalues\cleaned_employee_dataset.csv'
df = pd.read_csv(path)

plt.figure(figsize=(10, 6))
sns.boxplot(y=df["Performance Rating"])
plt.show()