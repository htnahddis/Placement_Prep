def bruteSort(arr):
    mid = 0
    low = 0 
    high = len(arr) -1

    while mid <= high:
        
        if arr[mid] == 1:
            mid += 1

        elif arr[mid] == 0:
            temp = arr[mid]
            arr[mid] = arr[low] 
            arr[low] = temp
            low +=1

        elif arr[mid] == 2:
            temp = arr[mid]
            arr[mid] = arr[high]
            arr[high] = temp
            high -=1
    return arr



arr = [1,0,2,0,0,0,1,0,1,2,2,2,2,1,0,1,0,1,1,1,2]
transfer = bruteSort(arr)
print(transfer)