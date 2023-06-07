def linear_search(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1


arr = [1, 3, 1, 6, 2, 7, 8]
n = len(arr)
n = linear_search(arr, n, x=6)
print(n)
