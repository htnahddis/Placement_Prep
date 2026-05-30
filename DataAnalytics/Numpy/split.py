import numpy as np 

arr = np.array([[1,2,3], [5,6,4]])


# arr1 = np.split(arr, 2) # splits the array into 2 equal parts
# print(arr1)

# arr2 = np.split(arr, [3,6]) # splits the array at the specified indices
# print(arr2)

# arr = np.vsplit(arr, 3) # splits the array vertically into 2 equal parts
# print(arr)

arr = np.hsplit(arr, 2) # splits the array horizontally into 2 equal parts
print(arr)
