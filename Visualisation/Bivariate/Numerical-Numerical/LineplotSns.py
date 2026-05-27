import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

"""
When to Use a Line Plot
Time-Series Data: Tracking variables over days, months, or years (e.g., stock prices, weather changes).
Continuous Variable Trends: Showing changes across a continuous scale (e.g., how reaction time changes with age).
Multiple Series Comparison: Comparing trends across a few different groups (e.g., comparing sales revenue of three separate products).
Rate of Change: Identifying how fast or slow a value is rising or falling over a specific period.

"""


path = r'Numpy\handlingmissingvalues\cleaned_employee_dataset.csv'
df = pd.read_csv(path)

plt.figure(figsize=(10, 6))
sns.lineplot(x=df["Age"], y=df["Salary (INR)"])
plt.title("Line Plot of Salary vs Age")         
plt.xlabel("Age")
plt.ylabel("Salary (INR)")
plt.show()
