def nge(arr: list)-> list:
    output = [0] * len(arr)
    i = 0
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[i] < arr[j]):
                output[i] = arr[j]
                break
    
    return output

arr = [2,3,1,3,0,0,5]
arr1 = nge(arr)
print(arr1)