def remove_value(arr, value):
    index = 0
    for i in range(len(arr)):
        if arr[i] != value:
            arr[index] = arr[i]
            index += 1
    arr.pop()


arr = [1, 2, 3, 4, 5]
remove_value(arr, 2)
print(arr)
