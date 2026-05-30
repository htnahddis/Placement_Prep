import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = r'Numpy\handlingmissingvalues\cleaned_employee_dataset.csv'

df = pd.read_csv(path)

x_bar = df['Department'].value_counts()
y_bar = df['Department'].value_counts().index

sns.countplot(x='Department', data=df, order=y_bar, palette='Set1')

plt.show()