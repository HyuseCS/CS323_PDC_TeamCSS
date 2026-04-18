def merge_sort(arr):
    # return if len(arr) <= 1
    if len(arr) <= 1:
        return arr
    
    # find the midpoint
    mid = len(arr) // 2

    # divide the array recursively 
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left_arr, right_arr):
    results = []

    # index count for each array
    left_count = right_count = 0

    # whichever first element of each array is smaller will get appended first to the results
    while left_count < len(left_arr) and right_count < len(right_arr):
        if left_arr[left_count] <= right_arr[right_count]:
            results.append(left_arr[left_count])
            left_count += 1
        else:
            results.append(right_arr[right_count])
            right_count += 1

    # push leftovers from either left or right array
    results += left_arr[left_count:]
    results += right_arr[right_count:]

    return results
        

print(merge_sort([5, 3, 8, 4, 9, 2, 7, 6, 1]))
# → [1, 2, 3, 4, 5, 7, 8, 9]