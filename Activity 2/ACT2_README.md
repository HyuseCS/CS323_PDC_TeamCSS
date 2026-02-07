1. Which approach demonstrates true parallelism in Python? Explain.

    The approach the demonstrates true parallelism is Multiprocessing. Because Python's threading module merely switches context between threads rapidly on  a single CPU core giving the illusion of doing things at the same time. Multiprocessing bypasses this by spawning separate memory spaces and processes to each with its own Python interpreter instance, allowing them to run on distinct CPU cores simultaneously.

2. Compare execution times between multithreading and multiprocessing.

    In almost every scenario involving lightweight tasks, multithreading significantly outperforms multiprocessing regarding the execution time. The difference is cause by an "overhead" thats an extra computing resources required to manage the code. Threads share the same memory space and belong to a single process, meaning they can be created and destroyed almost instantly. In Multiprocessing however, requires the operating system to allocate entirely new memory blocks and start a fresh instance of python interpreter for every single process.

3. Can Python handle true parallelism using threads? Why or why not?

    No, because of the Global Interperet Lock. The CPython interpreset uses mutex that prevents multiple native threads from executing Python bytecodes at once even if you have 100 threads on a 64-core machine.

4. What happens if you input a large number of grades (e.g., 1000)? Which method is faster and why?

    If I input 1000 grades using the same approach of "1 worker per grade", the difference in performance becomes clear and catastrophic. Multiprocessing will likely crash the machine or either execute extremely slowly because the operating system cannot efficiently handle the suddent creation of 1000 separate processes.
    Multithreading is faster in this specific scenario because creating 1000 threads is much 'cheaper' for the system than creating 1000 processes.

5. Which method is better for CPU-bound tasks and which for I/O-bound
tasks?

    Multiprocessing is the only valid choice for CPU-bound tasks as heavy computations like matrix multiplication, video rendering, or complex data analysis bypasses the GIL. This allows the code to run on multiple CPU cores simultaneously achieving true parallelism. Multithreading is superior for I/O-bound tasks as waiting operations like downloading files, querying a database, or getting user input. Since the CPU just sits idly while waiting for the tasks to finish.

6. How did your group apply creative coding or algorithmic solutions in this lab?

    We applied creative coding by rejecting the inefficient method of creating a new process for every single grade. We restructured the data into student-level batches and assigned one process to handle a full list of grades. For multithreading we implemented a responsive system where every new grade input immediately creates a separate thread to compute the GWA. This contrast demonstrated that threads are lightweight enough to spawn individually for rapid tasks unlike the heavier processes.

+-----------------+-----------------+------------+----------------+
| Method          | Execution Order | GWA Output | Execution Time |
+-----------------+-----------------+------------+----------------+
| Multithreading  |concurrent thread|            |                |
|                 | execcution      |  67.00     |0.001615 seconds|
+-----------------+-----------------+------------+----------------+
| Multiprocessing |parralel process |            |                |
|                 | execution       |  67.00     |0.029768 seconds|
+-----------------+-----------------+------------+----------------+