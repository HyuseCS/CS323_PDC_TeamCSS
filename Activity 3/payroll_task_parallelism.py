import threading
import time
from concurrent.futures import ThreadPoolExecutor

#Data
employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]

# Calculation Functions
def calculate_sss(salary):
    time.sleep(0.1)  #adds delay to simulate threads doing work since task is to small to show concurrency
    thread_name = threading.current_thread().name
    result = salary * 0.045
    print(f"  [ {thread_name} ] Calculating SSS...")
    return result

def calculate_philhealth(salary):
    time.sleep(0.1)
    thread_name = threading.current_thread().name
    result = salary * 0.025
    print(f"  [ {thread_name} ] Calculating PhilHealth...")
    return result

def calculate_pagibig(salary):
    time.sleep(0.1)
    thread_name = threading.current_thread().name
    result = salary * 0.02
    print(f"  [ {thread_name} ] Calculating Pag-IBIG...")
    return result

def calculate_tax(salary):
    time.sleep(0.1)
    thread_name = threading.current_thread().name
    result = salary * 0.1
    print(f"  [ {thread_name} ] Calculating Withholding Tax...")
    return result

# Processing Function
def process_employee(employee):
    name, salary = employee
    print(f"\n--- Processing: {name} (Salary: {salary:,.2f}) ---")

    with ThreadPoolExecutor(max_workers=4) as executor:
        # Using submit() to get Future objects
        future_sss = executor.submit(calculate_sss, salary)
        future_philhealth = executor.submit(calculate_philhealth, salary)
        future_pagibig = executor.submit(calculate_pagibig, salary)
        future_tax = executor.submit(calculate_tax, salary)

        # Retrieves results
        sss = future_sss.result()
        philhealth = future_philhealth.result()
        pagibig = future_pagibig.result()
        tax = future_tax.result()

    total_deductions = sss + philhealth + pagibig + tax
    net_pay = salary - total_deductions

    print(f"\n  Summary for {name}:")
    print(f"  SSS (4.5%):         {sss:10,.2f}")
    print(f"  PhilHealth (2.5%):  {philhealth:10,.2f}")
    print(f"  Pag-IBIG (2%):      {pagibig:10,.2f}")
    print(f"  Withholding Tax (10%): {tax:10,.2f}")
    print(f"  {' ' * 2}-{'-' * 30}")
    print(f"  Total Deduction:    {total_deductions:10,.2f}")
    print(f"  Net Pay:            {net_pay:10,.2f}")

# Main
if __name__ == "__main__":
    while True:
        print("\n=== Payroll Task Parallelism ===")
        print("Select an option:")
        for i, (name, salary) in enumerate(employees, 1):
            print(f"{i}. {name}")
        print(f"{len(employees) + 1}. Calculate All")
        print("0. Exit")

        try:
            choice = int(input("\nEnter choice: "))
            
            if choice == 0:
                break
            elif 1 <= choice <= len(employees):
                process_employee(employees[choice - 1])
            elif choice == len(employees) + 1:
                for emp in employees:
                    process_employee(emp)
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
