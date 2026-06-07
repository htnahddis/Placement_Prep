def bruteSort(arr):
    ans = []

    count0 = count1 = count2 = 0

    for num in arr:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    for _ in range(len(arr)):
        if count0:
            ans.append(0)
            count0 -= 1
        elif count1:
            ans.append(1)
            count1 -= 1
        else:
            ans.append(2)
            count2 -= 1

    return ans


arr = [1,0,2,0,0,0,1,0,1,2,2,2,2,1,0,1,0,1,1,1,2]
print(bruteSort(arr))