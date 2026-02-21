import time
import threading


def cook_rice(results):
    start = time.time()
    print("  -> Starting to cook rice...")
    results['rice'] = time.time() - start

def cook_egg(results):
    start = time.time()
    print("  -> Starting to cook egg...")
    results['egg'] = time.time() - start


def run_parallel():
    print("\n--- PARALLEL: Two Burners (Concurrent execution) ---")
    results = {}
    start_time = time.time()

    rice_worker.start()
    egg_worker.start()

    rice_worker.join()
    egg_worker.join()
    


if __name__ == "__main__":
    par_time, rice_time, egg_time = run_parallel()
    
    print("\n" + "="*40)
    print("PARALLEL EXECUTION REPORT")
    print("="*40)

