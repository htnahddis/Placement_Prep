import numpy as np 
import pandas as pd 

path = r'Numpy\handlingmissingvalues\augmented_dirty_employee_dataset.csv'

df = pd.read_csv(path) #why is this erro not abel to import? 
pd.options.mode.use_inf_as_na = True #treating inf values as nan values

print(df.head())

print("Identify missing values in the dataset:")
print(df.isnull().sum())

#replace ngative values with nan values
df = df.replace([np.inf, -np.inf], np.nan) 
# Works across all columns without crashing on text
df = df.map(lambda x: np.nan if isinstance(x, (int, float)) and x < 0 else x)
print("Identify missing values in the dataset:")
print(df.isnull().sum())
df = df.drop_duplicates() #drop duplicates


df['City'] = df['City'].fillna("Not Specified") #filling missing values with mode
df['Department'] = df['Department'].fillna("Not Specified") #filling missing values with mode

df[['Age', 'Experience (Years)' , 'Salary (INR)', 'Performance Rating']] = df[['Age', 'Experience (Years)', 'Salary (INR)', 'Performance Rating']].apply(pd.to_numeric, errors='coerce')

df['Age'] = df['Age'].fillna(df['Age'].mean()) #filling missing values with mean
df['Experience (Years)'] = df['Experience (Years)'].fillna(df['Experience (Years)'].mean()) #filling missing values with mean

#filling missing values with median

# 1. Calculate the mean and standard deviation of the column
salary_mean = df['Salary (INR)'].mean()
salary_std = df['Salary (INR)'].std()

# 2. Define your upper and lower boundaries
upper_bound = salary_mean + (3 * salary_std)
lower_bound = salary_mean - (3 * salary_std)

# 3. Identify outliers and replace them with the mean value
# This looks for values outside the bounds and swaps them with 'salary_mean'
df.loc[(df['Salary (INR)'] > upper_bound) | (df['Salary (INR)'] < lower_bound), 'Salary (INR)'] = salary_mean

df.loc[df['Performance Rating'] > 5, 'Performance Rating'] = df['Performance Rating'].median() #filling missing values with median

df['Performance Rating'] = df['Performance Rating'].fillna(df['Performance Rating'].median()) #filling missing values with median
df['Salary (INR)'] = df['Salary (INR)'].fillna(df['Salary (INR)'].mean()) #filling missing values with mean

print(df.isnull().sum())

df['Age'] =df['Age'].astype(int)

df.to_csv(r'Numpy\handlingmissingvalues\cleaned_employee_dataset.csv', index=False)

