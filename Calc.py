def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cant devide by zero"
    return x / y

# Main calc 
def calculator():
    while True:
        # print menu vir terminal
        print("\nMenu:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        choice = input("Choose an option from 1-5: ")

        # user input + operations
        if choice == '1':
            num1 = float(input("first number: "))
            num2 = float(input("second number: "))
            result = add(num1, num2)
            print(f"Result: {result}")
        elif choice == '2':
            num1 = float(input("first number: "))
            num2 = float(input("second number: "))
            result = subtract(num1, num2)
            print(f"Result: {result}")
        elif choice == '3':
            num1 = float(input("first number: "))
            num2 = float(input("second number: "))
            result = multiply(num1, num2)
            print(f"Result: {result}")
        elif choice == '4':
            num1 = float(input("dividend: "))
            num2 = float(input("divisor: "))
            result = divide(num1, num2)
            print(f"Result: {result}")
        elif choice == '5':
            print("Exiting calculator.")
            break
        else:
            print("Invalid, choose an option from 1 to 5.")

# run
calculator()