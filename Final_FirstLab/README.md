1. How did you distribute orders among worker processes?

We distributed orders among worker processes by having the master process (rank 0) send data to workers (ranks 1-3) individually. The orders were sent in a FCFS fashion.

2. What happens if there are more orders than workers?

IF there are more orders than workers, each worker would have to process more than one order. In this case, a worker finishes a task first before moving to the next one.

3. How did processing delays affect the order completion?

Orders with longer delays naturally end up finishing later. For two tasks A and B simultaneously processing, with B initializing 1 second later than A, if A took 4 seconds and B only 1, then B would complete first despite starting later.

4. How did you implement shared memory, and where was it initialized?

Shared memory was implemented using multiprocessing.Manager.list(). It was initialized after MPI.COMM_WORLD inside the 'if _name_ == "_main_"' block to ensure clean process separation and prevent MPI from freezing.

5. What issues occurred when multiple workers wrote to shared memory
simultaneously?

Having workers directly write to shared memory caused issues such as failing to properly populate data to the shared memory due to process management issues. It was very unreliable that we had to resort to having only the master process populate the shared memory, and workers only have to send finalized tasks to the master. This approach also allows us to forego the usage of Lock() because only the master is writing to the memory.

6. How did you ensure consistent results when using multiple processes?

We ensured consistent results by letting the master process write to the memory instead of workers writing directly to the shared memory. This prevents race conditions since only one process is writing to the memory, while still keeping the essence of distributed computing since the tasks are distributed individually to workers for processing.