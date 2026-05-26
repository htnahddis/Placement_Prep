
import numpy as np

arr = np.array([[1, 2], [3, 4]])    
arr1 = np.insert(arr, 1, [5, 6], axis=0)
print(arr1 )
print("\n" )

arr2 = np.concatenate((arr, arr1), axis=0)
print(arr2)
print("\n" )

arr3 = np.concatenate((arr, arr1), axis=)
print(arr3)
print("\n" )


#vstack and hstack are used to stack arrays vertically and horizontally respectively.
#difference between concatenate and vstack/hstack is that concatenate can be used to stack arrays along any axis, while vstack and hstack are specifically designed for vertical and horizontal stacking respectively.
arr4 = np.vstack((arr, arr1))
print(arr4)

arr5 = np.hstack((arr, arr1))
print(arr5)