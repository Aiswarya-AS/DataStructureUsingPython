def remove_duplicates(arr, n):
    unique = []
    for i in range(n):
        if arr[i] not in unique:
            unique.append(arr[i])
    return unique


my_array = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(my_array, len(my_array)))
