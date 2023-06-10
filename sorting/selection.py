def selection_sort(arr, n):
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


arr = [5, 1, 4, 2, 9, 8]
n = len(arr)
selection_sort(arr, n)
print(arr)
