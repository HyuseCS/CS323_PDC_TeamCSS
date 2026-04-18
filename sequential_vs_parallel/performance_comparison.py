from parallel_sort import parallel_merge_sort
from sequential_sort import merge_sort
from sequential_search import linear_search
from parallel_search import worker
from multiprocessing import Process, Queue
import random, time

def parallel_search_wrapper(data, target):
    """
    Wrapper function to execute the worker from parallel_search.py
    and return the index of the found target instead of just printing it.
    """
    q = Queue()
    chunk_size = len(data) // 4
    if chunk_size == 0: chunk_size = 1
    processes = []
    
    for j in range(0, len(data), chunk_size):
        sub_data = data[j : j + chunk_size]        
        p = Process(target=worker, args=(sub_data, target, q, j))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    # Return the index if found by any worker, otherwise return -1
    if not q.empty():
        return q.get()
    return -1

def main():
    sizes = {
        "Small": 1000,
        "Medium": 100000,
        "Large": 1000000
    }

    # =========================================================
    # SORTING EVALUATION
    # =========================================================
    print("--- Sequential vs. Parallel Merge Sort Evaluation ---")

    for name, size in sizes.items():
        print(f"\nEvaluating {name} Dataset ({size} elements):")
        
        # Random Data
        data = [random.randint(1, 1000000) for _ in range(size)]
        chunk_size = size // 4  
        
        parallel_start = time.time()
        sorted_data_par = parallel_merge_sort(data, chunk_size)
        parallel_end = time.time()

        sequential_start = time.time()
        sorted_data_seq = merge_sort(data)
        sequential_end = time.time()
        
        # Correctness verification
        is_correct = sorted_data_par == sorted(data)
        print("Parallel Sort:")
        print(f"  Random Data:         {parallel_end - parallel_start:.4f} seconds (Correct: {is_correct})")

        # Already Sorted Data
        parallel_start = time.time()
        sorted_data_2 = parallel_merge_sort(sorted_data_par, chunk_size)
        parallel_end = time.time()
        print(f"  Already Sorted Data: {parallel_end - parallel_start:.4f} seconds")

        # Reverse sorted data
        reverse_data = sorted_data_par[::-1]
        parallel_start = time.time()
        sorted_data_3 = parallel_merge_sort(reverse_data, chunk_size)
        parallel_end = time.time()
        print(f"  Reverse Sorted Data: {parallel_end - parallel_start:.4f} seconds")

        print("\nSequential Sort:")
        sequential_start = time.time()
        sorted_data_seq = merge_sort(data)
        sequential_end = time.time()
        print(f"  Random Data:         {sequential_end - sequential_start:.4f} seconds")

        sequential_start = time.time()
        sorted_data_2 = merge_sort(sorted_data_seq)
        sequential_end = time.time()
        print(f"  Already Sorted Data: {sequential_end - sequential_start:.4f} seconds")    

        reverse_data = sorted_data_seq[::-1]
        sequential_start = time.time()
        sorted_data_3 = merge_sort(reverse_data)
        sequential_end = time.time()
        print(f"  Reverse Sorted Data: {sequential_end - sequential_start:.4f} seconds")

    # =========================================================
    # SEARCHING EVALUATION
    # =========================================================
    print("\n\n--- Sequential vs. Parallel Linear Search Evaluation ---")
    
    for name, size in sizes.items():
        print(f"\nEvaluating {name} Dataset ({size} elements):")
        
        data = [random.randint(1, 1000000) for _ in range(size)]
        
        # Use the last element as target to simulate a worst-case scenario for traversing
        target = data[-1] 
        
        parallel_start = time.time()
        found_index_par = parallel_search_wrapper(data, target)
        parallel_end = time.time()

        sequential_start = time.time()
        found_index_seq = linear_search(data, target)
        sequential_end = time.time()
        
        # Correctness verification for search
        is_correct = (found_index_par != -1) and (data[found_index_par] == target)
        print("Parallel Search:")
        print(f"  Random Data:         {parallel_end - parallel_start:.6f} seconds (Correct: {is_correct})")

        sorted_data = sorted(data)
        target_sorted = sorted_data[-1]
        
        parallel_start = time.time()
        found_index_par_2 = parallel_search_wrapper(sorted_data, target_sorted)
        parallel_end = time.time()
        print(f"  Already Sorted Data: {parallel_end - parallel_start:.6f} seconds")

        reverse_data = sorted_data[::-1]
        target_reverse = reverse_data[-1] 
        
        parallel_start = time.time()
        found_index_par_3 = parallel_search_wrapper(reverse_data, target_reverse)
        parallel_end = time.time()
        print(f"  Reverse Sorted Data: {parallel_end - parallel_start:.6f} seconds")

        print("\nSequential Search:")
        print(f"  Random Data:         {sequential_end - sequential_start:.6f} seconds")

        sequential_start = time.time()
        found_index_seq_2 = linear_search(sorted_data, target_sorted)
        sequential_end = time.time()
        print(f"  Already Sorted Data: {sequential_end - sequential_start:.6f} seconds")

        sequential_start = time.time()
        found_index_seq_3 = linear_search(reverse_data, target_reverse)
        sequential_end = time.time()
        print(f"  Reverse Sorted Data: {sequential_end - sequential_start:.6f} seconds")


if __name__ == "__main__":
    main()