num1 = int(input("Enter the first number: ").strip())
num2 = int(input("Enter the second number: ").strip())
operation = input("Choose the operation (+, -, *, /): ").strip()

match operation:
    case '+':
        print(f" The result is {eval('num1 + num2')}")
    case '-':
        print(f" The result is {eval('num1 - num2')}")
    case '*':
        print(f" The result is {eval('num1 * num2')}")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f" The result is {eval('num1 // num2')}")
