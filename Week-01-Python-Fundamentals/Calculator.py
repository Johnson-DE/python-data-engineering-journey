try:
    a = float(input("Enter a Number: "))
    b = float(input("Enter a Number: "))
    op = input("Enter a operation(+, -, *, /): ")
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b
    else:
        print("Invalid Operation")
        result = None
    if result is not None:
        print("Result: ", result)
except ValueError:
    print("Enter Numbers Only")
except ZeroDivisionError:
    print("Cannot  do Division by Zero")
finally:
    print("Program Completed")