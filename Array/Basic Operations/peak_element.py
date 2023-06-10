def peak_element(arr, low, high, n):
    mid = low + (high - low) // 2

    if (mid == 0 or arr[mid - 1] < arr[mid]) and (
        mid == n - 1 or arr[mid] > arr[mid + 1]
    ):
        return mid
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return peak_element(arr, low, mid - 1, n)
    else:
        return peak_element(arr, mid + 1, high, n)


arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print("The index with the peak element is", peak_element(arr, 0, n - 1, n))
