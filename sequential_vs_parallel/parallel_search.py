from multiprocessing import Process, Queue
import random
import time

def worker(sub_data, target, q, offset):
    for i in range(len(sub_data)):
        if sub_data[i] == target:

            global_index = i + offset
            q.put(global_index)

            return
def tests(N, testname, is_sorted = False):
    print("running dataset", testname, "with", N, "elements")
    data = [random.randint(1, 1000000) for _ in range(N)] 
    
    if is_sorted:
        data.sort() 
    target = random.choice(data)
    print(f"Target: {target}")
    
    q = Queue()
    chunk_size = len(data) // 4
    processes = []
    start = time.time()

    for j in range(0, len(data), chunk_size):
        
        sub_data = data[j : j + chunk_size]        
        p = Process(target=worker, args=(sub_data, target, q, j))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    end = time.time()

    time_taken = end - start
    if q.empty() == True:
        print("target not found")
        print("time taken: ", time_taken)
        print("------------------------------------------------------------------------")

    else:
        found_index = q.get()
        print(f"target found at: {found_index}")
        print("time taken: ", time_taken)
        print("------------------------------------------------------------------------")

if __name__ == '__main__':
    tests(1000, "small")
    time.sleep(2)
    tests(100000, "medium")
    time.sleep(2)
    tests(1000000, "large")
    time.sleep(2)
    tests(1000000, "spisyal", is_sorted=True)