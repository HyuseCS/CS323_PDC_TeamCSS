# Calculator Made by Team CSS

def get_input(text):
    while (True):
        try:
            num = float(input(text))
            break
        except(TypeError, ValueError):
            pass    
    return num

def addition(num1, num2):
    sum = num1 + num2
    print(f"\n\nThe sum of {num1} and {num2} is {sum}.\n\n")

def subtraction(num1, num2):
    difference = num1 - num2
    print(f"\n\nThe difference of {num1} and {num2} is {difference}.\n\n")
    
def multiplication(num1, num2):
    product = num1 * num2
    print(f"\n\nThe product of {num1} and {num2} is {product}.\n\n")

while(True):
    print("This is a simple floating point integer calculator")
    print("Choices: ")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = get_input("\nWhat would you like to do? Input the number of the operation: ")

    match choice:
        case 1:
            num1 = get_input("Input the first number: ")
            num2 = get_input("Input the second number: ")
            addition(num1, num2)
            continue
        case 2:
            num1 = get_input("Input the first number: ")
            num2 = get_input("Input the second number: ")
            subtraction(num1, num2)
            continue
        case 3:
            num1 = get_input("Input the first number: ")
            num2 = get_input("Input the second number: ")
            multiplication(num1, num2)
            continue
        case 4:
            continue
        case 5:
            break
        case _:
            print("Choice not found. Try again")
            continue
