def deletion(arr, index):
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr.pop()


arr = [1, 2, 3, 4, 5]
deletion(arr, 2)
print(arr)
