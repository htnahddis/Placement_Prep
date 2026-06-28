arr = [1, 2, 3]


def permute(arr, index):
    if index == len(arr):
        print(arr)
        return

    for i in range(index, len(arr)):
        # Swap
        arr[index], arr[i] = arr[i], arr[index]
        print(arr[index], arr[i])

        # Recurse
        permute(arr, index + 1)

        # Backtrack (swap back)
        arr[index], arr[i] = arr[i], arr[index]


permute(arr, 0)

