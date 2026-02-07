import threading
import time

# 1. Reuse the Input Logic (Same as Multiprocessing for fairness)
def input_grades(num_students, num_subjects):
    matrix = []
    print(f"\n--- Grade Entry Phase ({num_students} students) ---")
    for i in range(num_students):
        while True:
            try:
                user_input = input(f"Student {i + 1}: Enter {num_subjects} grades (space separated): ").strip()
                grades = [float(g) for g in user_input.split()]
                if len(grades) != num_subjects:
                    print(f"Error: Entered {len(grades)} grades. Need {num_subjects}.")
                    continue
                matrix.append(grades)
                break
            except ValueError:
                print("Invalid input.")
    return matrix

# 2. The Worker Function (Target for Threads)
def compute_gwa(grades, student_id):
    # Simulate a tiny delay so you can see threads interleaving
    time.sleep(0.001) 
    
    if not grades:
        gwa = 0.0
    else:
        gwa = sum(grades) / len(grades)
    
    # Print immediately to show concurrency
    print(f"[Thread-{student_id}] Student {student_id} GWA: {gwa:.2f}")

def main():
    print("Multithreading Grade Calculator")
    
    try:
        n_students = int(input("How many students? "))
        n_subjects = int(input("How many subjects per student? "))
        
        # Phase 1: Input
        student_matrix = input_grades(n_students, n_subjects)
        
        print(f"\n--- Threading Phase (Simultaneous) ---")
        threads = []
        
        # Phase 2: Create Threads (1 Thread per Student)
        for i, student_grades in enumerate(student_matrix):
            t = threading.Thread(target=compute_gwa, args=(student_grades, i+1))
            threads.append(t)
            
        start = time.time()
        
        # Start all threads
        for t in threads:
            t.start()
            
        # Wait for all to finish
        for t in threads:
            t.join()
            
        end = time.time()
        
        print(f"\nTime Taken: {end - start:.6f} seconds")
        
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()