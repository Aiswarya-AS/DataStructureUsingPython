def bubble_sort(arr, n):
    for i in range(n):
        flag = 0
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1
        if flag == 0:
            break


arr = [5, 1, 4, 2, 9, 8]
n = len(arr)
bubble_sort(arr, n)
print(arr)
