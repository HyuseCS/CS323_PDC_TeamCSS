from mpi4py import MPI
from multiprocessing import Manager
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

ITEMS = [
    f"Mechanical Keyboard (75% Layout)",
    "USB-C Docking Station",
    "Active Noise-Cancelling Earbuds",
    "Portable Power Bank (20,000mAh)"
]

def main():
    # 1. Initialize the multiprocessing Manager and shared list
    manager = Manager()
    shared_orders = manager.list()

    # master
    if rank == 0:
        worker_assigned = 1
        
        # generate 8 orders
        for i in range(8):
            generate_order(i, worker_assigned)

            worker_assigned += 1
            if worker_assigned >= size:
                worker_assigned = 1

        terminate_workers()

        # Wait for all workers to finish appending before printing the final list
        comm.Barrier()
        
        # 2. Master collects and prints the complete list of orders
        print("\n--- Final Completed Orders in Shared Memory ---")
        for completed_order in shared_orders:
            print(completed_order)

    # worker
    else:
        while True:
            data = comm.recv(source=0)

            if data == "TERMINATE":
                break
            
            print(f"Worker {rank} processing item {data['item_name']} (Order ID: {data['order_id']})")
            
            # 3. Workers append processed orders to the shared structure
            shared_orders.append(data)
                
        # Sync up with the master process once the while loop breaks
        comm.Barrier()


def generate_order(order_id, worker_assigned):
    order = {'order_id': order_id, 'item_name': ITEMS[random.randint(0, 3)]} 
    comm.send(order, dest=worker_assigned)


def terminate_workers():
    for worker_id in range(1, size):
        comm.send("TERMINATE", worker_id)


if _name_ == '_main_':
    main()