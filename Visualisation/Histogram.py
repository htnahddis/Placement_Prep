import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

"""
Default values in y axis in histogram are counts
if you have otuliers mean != median != mode, if you have normal distribution mean = median = mode,
 if you have left skewed distribution mean < median < mode, if you have right skewed distribution mean > median > mode
"""

#Skwed distribution: left skewed distribution, right skewed distribution, normal distribution

# 
path = r'Numpy\handlingmissingvalues\cleaned_employee_dataset.csv'
df = pd.read_csv(path)

df["Department"] = df["Department"].replace({
    "it": "IT",
    "It": "IT",
    "Hr": "HR",
    "Finance": "FINANCE"
})

#the distance between bins can be reduced
plt.figure(figsize=(10, 6))

plt.hist(df["Salary (INR)"], bins=10, edgecolor='black')
plt.title("Distribution of Salary") 
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.xticks(rotation=45, ha='right')
plt.show()

