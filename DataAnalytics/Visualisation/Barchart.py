
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

"""
Data Visualization with Matplotlib and Seaborn
Anatomy of a plot: legend, axes, title, labels, axis ticks, grid, figure, subplot
Matplotlib: A powerful and flexible library for creating static, animated, and interactive visualizations in Python. It provides a wide range of plotting functions and customization options.
Seaborn: A statistical data visualization library built on top of Matplotlib. It provides a high-level interface for creating attractive and informative statistical graphics. Seaborn is particularly useful for visualizing complex datasets and performing exploratory data analysis.
"""

"""
Types of columns
1. Categorical columns: These columns contain discrete values that represent categories or groups. Examples include 'City', 'Department', and 'Performance Rating'.
2. Numerical columns: These columns contain continuous or discrete numerical values. Examples include 'Age',

In categorical columns
1. Nominal columns: These columns contain categories that have no inherent order or ranking. Examples include 'City' and 'Department'.
2. Ordinal columns: These columns contain categories that have a specific order or ranking. An example is 'Performance Rating', which may have values like 'Poor', 'Average', 'Good', 'Excellent' that indicate a ranking.
3. Binary columns: These columns contain only two categories, often represented as 0 and 1. An example could be a column indicating whether an employee is a manager (1) or not (0).

In numerical columns
1. Continuous columns: These columns can take any value within a range. Examples include 'Age' and 'Salary (INR)'.
2. Discrete columns: These columns can only take specific, separate values. An example is 'Experience (Years)', which may only take integer values. 
3. Count columns: These columns represent counts of occurrences or events. An example could be a column indicating the number of projects an employee has worked on.
4. Ratio columns: These columns represent ratios or proportions. An example could be a column indicating the ratio of completed projects to total projects for an employee.
5. Interval columns: These columns represent values that have meaningful intervals but no true zero point. An example could be a column indicating the number of hours an employee works per week, where 0 does not necessarily mean the absence of work.
6. Time series columns: These columns represent data points collected or recorded at specific time intervals. An example could be a column indicating the date of hire for each employee.
7. Percentage columns: These columns represent values as percentages. An example could be a column indicating the percentage of tasks completed by an employee.
8. Currency columns: These columns represent monetary values. An example is 'Salary (INR)', which indicates the salary of each employee in Indian Rupees.



"""
path = r'Numpy\handlingmissingvalues\cleaned_employee_dataset.csv'

df = pd.read_csv(path) 


"""
Types of plot 
-> Univariate plots: These plots are used to visualize the distribution of a single variable. Examples include histograms, box plots, and density plots.
-> Bivariate plots: These plots are used to visualize the relationship between two variables. Examples include scatter plots, line plots, and bar plots.
-> Multivariate plots: These plots are used to visualize the relationships between three or more variables. Examples include pair plots, heatmaps, and 3D scatter plots.

"""




x_bar = df['Department'].value_counts()
y_bar = df['Department'].value_counts().index

# Create figure FIRST
plt.figure(figsize=(10,6))

#issue that was raised here was we need to create the figure before plotting, otherwise it will not work. So we need to create the figure first and then plot.
#because when we create the figure, it creates a new figure and then when we plot, it plots on that figure. If we plot first and then create the figure, it will plot on the default figure and then when we create the figure, it will create a new figure and the plot will not be visible on that new figure. So we need to create the figure first and then plot on that figure.

# Then plot
plt.bar(y_bar, x_bar, color='blue', edgecolor='black')

# Customization
plt.xticks(rotation=45, ha='right', fontsize=10,
           color='blue', fontweight='bold')

plt.xlabel('Department', fontsize=12,
           color='red', fontweight='bold')

plt.ylabel('Count', fontsize=12,
           color='red', fontweight='bold')

plt.title('Count of Employees in Each Department')

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()


sns.countplot(x='Department', data=df, palette='Set2')
plt.xticks(rotation=45, ha='right', fontsize=10,    color='blue', fontweight='bold')
plt.xlabel('Department', fontsize=12, color='red', fontweight='bold')               
plt.ylabel('Count', fontsize=12, color='red', fontweight='bold')
plt.title('Count of Employees in Each Department')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
