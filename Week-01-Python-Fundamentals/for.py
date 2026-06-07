try:
    a = int(input("Enter a Number: "))
    b = int(input("Enter a Number: "))
    print(a/b)
except ValueError:
    print("Enter Numbers Only")
except ZeroDivisionError:
    print("Cannot divide by Zero")
finally:
    print("Program Completed")
