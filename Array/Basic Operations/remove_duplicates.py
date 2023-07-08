def remove_duplicates(arr):
    unique_index = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[unique_index]:
            unique_index += 1
            arr[unique_index] = arr[i]
    del arr[unique_index + 1:]
    return arr


my_array = [1, 2, 2, 3, 4, 4, 5, 6, 6]
result = remove_duplicates(my_array)
print(result)
