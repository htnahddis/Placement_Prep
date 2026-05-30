import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

"""
Piechart is used when we hear the word distribution, we think of pie chart. Pie chart is used to show the distribution of a categorical variable. It is a circular chart divided into sectors, where each sector represents a proportion of the whole. The size of each sector is proportional to the quantity it represents. Pie charts are useful for showing the relative proportions of different categories in a dataset, making it easy to compare the sizes of different groups at a glance.
Piechart is only in matplotlib 
"""

path = r'Numpy\handlingmissingvalues\cleaned_employee_dataset.csv'
df = pd.read_csv(path)

df["Department"] = df["Department"].replace({
    "it": "IT",
    "It": "IT",
    "Hr": "HR",
    "Finance": "FINANCE"
})

department_salaries = df.groupby('Department')['Salary (INR)'].sum().reset_index()

plt.pie(department_salaries['Salary (INR)'], labels=department_salaries['Department'], autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Total Salaries by Department')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()