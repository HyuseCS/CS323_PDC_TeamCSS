import threading

FINAL_GWA = 0
LOCK = threading.Lock()

def compute_gwa(grades):
    global FINAL_GWA
    
    gwa = sum(grades) / len(grades)
    
    print(f"[Thread] Calculated GWA: {gwa}")

    with LOCK:
        FINAL_GWA = gwa

# Ensure the input is a number
def get_number(input_text):
    while True:
        try:
            number = int(input(input_text))
            break
        except (TypeError, ValueError):
            pass
    return number

def main():
    grades_list = [] 

    grades_count = get_number("Number of grades: ")
    threads = []
    
    for _ in range(grades_count):
        grades_list.append(get_number("Enter grade: "))
        t = threading.Thread(target=compute_gwa, args=(grades_list,))
        threads.append(t)
    
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Final GWA:", FINAL_GWA) 


if __name__ == "__main__":
    main()