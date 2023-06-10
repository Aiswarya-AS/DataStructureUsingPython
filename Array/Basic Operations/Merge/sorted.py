def merge_array(arr1, arr2, arr3, n1, n2):
    i, j, k = 0, 0, 0
    while i < n1:
        arr3[k] = arr1[i]
        i += 1
        k += 1
    while j < n2:
        arr3[k] = arr2[j]
        j += 1
        k += 1


arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [7, 8, 9, 10, 11, 12]
n1 = len(arr1)
n2 = len(arr2)
arr3 = [0 for i in range(n1 + n2)]
merge_array(arr1, arr2, arr3, n1, n2)
print(arr3)
