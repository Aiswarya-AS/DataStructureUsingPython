def insertion(arr, index, num):
    arr.append(None)
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = num


arr = [1, 2, 3, 4, 5]
insertion(arr, 2, 100)
print(arr)
