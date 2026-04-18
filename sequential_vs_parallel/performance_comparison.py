from parallel_sort import parallel_merge_sort
from sequential_sort import merge_sort
import random, time

def main():
    sizes = {
        "Small": 1000,
        "Medium": 100000,
        "Large": 1000000
    }

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
        print("Parallel:")
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

        print("\nSequential:")
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

if __name__ == "__main__":
    main()