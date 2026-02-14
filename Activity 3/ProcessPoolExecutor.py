from concurrent.futures import ProcessPoolExecutor

SSS_RATE = 0.045
PHILHEALTH_RATE = 0.025
PAGIBIG_RATE = 0.02
TAX_RATE = 0.10

employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]

def compute_payroll(employee):
    name, gross_salary = employee
    
    sss_deduction = gross_salary * SSS_RATE
    philhealth_deduction = gross_salary * PHILHEALTH_RATE
    pagibig_deduction = gross_salary * PAGIBIG_RATE
    tax_deduction = gross_salary * TAX_RATE
    
    total_deduction = sss_deduction + philhealth_deduction + pagibig_deduction + tax_deduction
    net_salary = gross_salary - total_deduction
    
    return name, gross_salary, total_deduction, net_salary

if __name__ == '__main__':
    print("--- Payroll Computation using Data Parallelism ---")
    
    with ProcessPoolExecutor() as executor:
        results = executor.map(compute_payroll, employees)
        
        for result in results:
            name, gross_salary, total_deduction, net_salary = result
            print(f"Employee: {name}")
            print(f"  Gross Salary:    ₱{gross_salary:,.2f}")
            print(f"  Total Deduction: ₱{total_deduction:,.2f}")
            print(f"  Net Salary:      ₱{net_salary:,.2f}")
            print("-" * 40)