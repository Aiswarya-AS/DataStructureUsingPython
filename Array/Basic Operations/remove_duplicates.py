# for sorted lists
# def remove_duplicates(arr):
#     unique_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] != arr[unique_index]:
#             unique_index += 1
#             arr[unique_index] = arr[i]
#     del arr[unique_index + 1:]
#     return arr[:unique_index + 1]


# my_array = [1, 2, 2, 3, 4, 4, 5, 6, 6]
# result = remove_duplicates(my_array)
# print(result)


def remove_duplicates(arr):
    if len(arr) == 0:
        return arr

    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                arr[j] = None  # Mark duplicates for removal

    # Filter out the None values
    arr = [x for x in arr if x is not None]
    return arr


my_array = [1, 2, 2, 3, 4, 4, 5, 6, 6]
result = remove_duplicates(my_array)
print(result)
