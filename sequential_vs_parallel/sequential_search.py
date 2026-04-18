import random
import time

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

def evaluate_search():
    sizes = {
        "Small": 1000,
        "Medium": 100000,
        "Large": 1000000
    }

    print("Sequential Linear Search Evaluation")
    for name, size in sizes.items():
        print(f"\nEvaluating {name} Dataset ({size} elements):")
        data = [random.randint(1, 1000000) for _ in range(size)]
        
        target = data[-1] 
        
        start = time.time()
        found_index = linear_search(data, target)
        end = time.time()
        
        is_correct = found_index == (size - 1)
        print(f"Random Data:         {end - start:.6f} seconds (Correct: {is_correct})")

        sorted_data = sorted(data)
        target_sorted = sorted_data[-1]
        
        start = time.time()
        found_index_2 = linear_search(sorted_data, target_sorted)
        end = time.time()
        print(f"Already Sorted Data: {end - start:.6f} seconds")

        reverse_data = sorted_data[::-1]
        target_reverse = reverse_data[-1] 
        
        start = time.time()
        found_index_3 = linear_search(reverse_data, target_reverse)
        end = time.time()
        print(f"Reverse Sorted Data: {end - start:.6f} seconds")

if __name__ == "__main__":
    evaluate_search()