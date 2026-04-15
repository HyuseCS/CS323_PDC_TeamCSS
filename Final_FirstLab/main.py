import multiprocessing
import random
import time

# The Goal: Use a Manager list for shared memory without freezing MPI.
# We initialize inside the __main__ block to ensure clean process separation.

if __name__ == '__main__':
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    manager = multiprocessing.Manager()
    shared_orders = manager.list()

    ITEMS = [
        "Mechanical Keyboard (75% Layout)",
        "USB-C Docking Station",
        "Active Noise-Cancelling Earbuds",
        "Portable Power Bank (20,000mAh)"
    ]

    # Rank 0 (Master) manages the shared list
    if rank == 0:
        print(f"Master (Rank 0): Starting Manager Server...")
        print(f"Master (Rank 0): Manager is ready.")
        
        try:
            # Distribute 8 orders to workers
            for i in range(8):
                worker_id = (i % (size - 1)) + 1
                order = {'order_id': i, 'item_name': random.choice(ITEMS)}
                comm.send(order, dest=worker_id)

            # Collect reports back from workers and store in shared memory
            print(f"Master (Rank 0): Waiting for results...")
            for i in range(8):
                processed_data = comm.recv(source=MPI.ANY_SOURCE)
                
                # Critical Section: Adding data to the shared Manager structure
                shared_orders.append(processed_data)
                print(f"Master (Rank 0): Progress {i+1}/8")

            # Signal workers to finish
            for worker_id in range(1, size):
                comm.send("TERMINATE", dest=worker_id)

            
            print("\n--- Final Completed Orders in Shared Memory ---")
            for completed_order in shared_orders:
                print(completed_order)
                
        finally:
            # Explicitly shut down the manager to release the port/socket
            manager.shutdown()
            print("Master (Rank 0): Manager shut down successfully.")
            
    else:
        # Worker logic 
        while True:
            data = comm.recv(source=0)
            if data == "TERMINATE":
                break
            
            print(f"Worker {rank} processing item {data['item_name']} (Order ID: {data['order_id']})")
            
            # delay
            delay = random.randint(1, 3)
            time.sleep(delay)  
            print(f"Worker {rank} finished processing item {data['item_name']} (Order ID: {data['order_id']}) (Time elapsed: {delay} seconds)")
            
            # Sends results back to Master to be stored in the Manager list
            comm.send(data, dest=0)
