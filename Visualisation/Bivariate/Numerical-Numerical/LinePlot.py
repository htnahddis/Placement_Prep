import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


path = r'Numpy\handlingmissingvalues\cleaned_employee_dataset.csv'
df = pd.read_csv(path)
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 6, 7]

# Create line plot
plt.plot(x, y)

# Add context
plt.title("Sample Line Plot")
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")

# Display
plt.show()
