def binary_saerch(arr, n, x):
    low = 0
    high = n - 1
    mid = 0

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


arr = [2, 3, 4, 10, 40]
x = 10
n = len(arr)
result = binary_saerch(arr, n, x)
if result != -1:
    print("Element found at the index", result)
else:
    print("element not found")
