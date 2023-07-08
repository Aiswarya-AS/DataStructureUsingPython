def build_min_heap(nums):
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)


def heapify(nums, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and nums[left] < nums[smallest]:
        smallest = left

    if right < n and nums[right] < nums[smallest]:
        smallest = right

    if smallest != i:
        nums[i], nums[smallest] = nums[smallest], nums[i]
        heapify(nums, n, smallest)


def find_kth_largest(nums, k):
    build_min_heap(nums)
    for i in range(k):
        result = nums[0]
        nums[0] = nums[-1]
        nums.pop()
        heapify(nums, len(nums), 0)
    return result


def find_kth_smallest(nums, k):
    build_min_heap(nums)
    for i in range(len(nums) - k):
        nums[0], nums[-1] = nums[-1], nums[0]
        nums.pop()
        heapify(nums, len(nums), 0)
    return nums[0]


# Example usage
nums = [4, 2, 7, 1, 5, 9]
k = 3

kth_largest = find_kth_largest(nums, k)
kth_smallest = find_kth_smallest(nums, k)

print("Kth largest:", kth_largest)
print("Kth smallest:", kth_smallest)
