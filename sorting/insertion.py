def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


arr = [5, 1, 4, 2, 9, 8]
n = len(arr)
insertion_sort(arr, n)
print(arr)
