import random
import time

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

def evaluate_sort():
    sizes = {
        "Small": 1000,
        "Medium": 100000,
        "Large": 1000000
    }

    print("--- Sequential Merge Sort Evaluation ---")

    for name, size in sizes.items():
        print(f"\nEvaluating {name} Dataset ({size} elements):")
        
        # Random Data
        data = [random.randint(1, 1000000) for _ in range(size)]
        
        start = time.time()
        sorted_data = merge_sort(data)
        end = time.time()
        
        # Correctness verification
        is_correct = sorted_data == sorted(data)
        print(f"  Random Data:         {end - start:.4f} seconds (Correct: {is_correct})")

        # Already Sorted Data
        start = time.time()
        sorted_data_2 = merge_sort(sorted_data)
        end = time.time()
        print(f"  Already Sorted Data: {end - start:.4f} seconds")

        # Reverse sorted data
        reverse_data = sorted_data[::-1]
        start = time.time()
        sorted_data_3 = merge_sort(reverse_data)
        end = time.time()
        print(f"  Reverse Sorted Data: {end - start:.4f} seconds")

if __name__ == "__main__":
    # Test if memory issues with recursion limit occur on Large dataset.
    import sys
    sys.setrecursionlimit(2000000) # Recursion limit increased just in case, though max depth for 1M is ~20
    
    evaluate_sort()
