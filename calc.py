def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Division by zero is not allowed."

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Enter a choice (1/2/3/4/5): ")
    
    if choice in ('1', '2', '3', '4'):  # Fixed choice comparison
        x = int(input("Enter num1: "))
        y = int(input("Enter num2: "))
        
        if choice == '1':
            print("Result:", add(x, y))
        elif choice == '2':
            print("Result:", sub(x, y))
        elif choice == '3':
            print("Result:", mul(x, y))
        elif choice == '4':
            print("Result:", div(x, y))
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid Operation Input.")
