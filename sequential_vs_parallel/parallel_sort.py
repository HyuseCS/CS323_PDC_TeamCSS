import multiprocessing, random, time


def main():
    sizes = {
        "Small": 1000,
        "Medium": 100000,
        "Large": 1000000
    }

    print("--- Parallel Merge Sort Evaluation ---")

    for name, size in sizes.items():
        print(f"\nEvaluating {name} Dataset ({size} elements):")
        
        # Random Data
        data = [random.randint(1, 1000000) for _ in range(size)]
        chunk_size = size // 4  
        
        start = time.time()
        sorted_data = parallel_merge_sort(data, chunk_size)
        end = time.time()
        
        # Correctness verification
        is_correct = sorted_data == sorted(data)
        print(f"  Random Data:         {end - start:.4f} seconds (Correct: {is_correct})")

        # Already Sorted Data
        start = time.time()
        sorted_data_2 = parallel_merge_sort(sorted_data, chunk_size)
        end = time.time()
        print(f"  Already Sorted Data: {end - start:.4f} seconds")

        # Reverse sorted data
        reverse_data = sorted_data[::-1]
        start = time.time()
        sorted_data_3 = parallel_merge_sort(reverse_data, chunk_size)
        end = time.time()
        print(f"  Reverse Sorted Data: {end - start:.4f} seconds")


def merge_sort(arr):
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


def parallel_merge_sort(arr, chunk_size):
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    with multiprocessing.Pool(processes=4) as pool:
        # Sort chunks in parallel
        sorted_chunks = pool.map(merge_sort, chunks)

        # Merge sorted chunks sequentially 
        while len(sorted_chunks) > 1:
            merged_chunks = []

            for i in range(0, len(sorted_chunks)-1, 2):
                merged_chunks.append(merge(sorted_chunks[i], sorted_chunks[i + 1]))

            if len(sorted_chunks) % 2 == 1:
                merged_chunks.append(sorted_chunks[-1])

            sorted_chunks = merged_chunks

        return sorted_chunks[0]

if __name__ == "__main__":
    main()
    

    
        
    