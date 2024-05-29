
# merge sort without recurrence....
def merge(arr, left, mid, right):
    # Create temporary arrays to hold the two halves
    s1 = mid - left + 1
    s2 = right - mid
    left_arr = [0] * s1
    right_arr = [0] * s2
    for i in range(s1):
        left_arr[i] = arr[left + i]
    for j in range(s2):
        right_arr[j] = arr[mid + 1 + j]
    i = j = 0
    k = left
    while i < s1 and j < s2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < s1:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < s2:
        arr[k] = right_arr[j]
        j += 1
        k += 1
def iterative_merge_sort(arr):
    n = len(arr)
    curr_size = 1
    while curr_size < n:
        left_start = 0
        while left_start < n - 1:
            mid = min(left_start + curr_size - 1, n - 1)
            right_end = min(left_start + 2 * curr_size - 1, n - 1)
            merge(arr, left_start, mid, right_end)
            left_start += 2 * curr_size
        curr_size *= 2

arr = [12,30,2,45,12,1]
iterative_merge_sort(arr)
print("Sorted array using merge sort:",arr)