# Topic 1: Exception Handling
# Practice 1

"""try:
    age = int(input("Enter Your Age: "))

except ValueError:
    print("Enter Numbers Only")

else:
    print("Your age is ", age)"""

# Practice 2
# Calculator

"""try: 
    num1 = int(input("Enter Number1: "))
    num2 = int(input("Enter Number2: "))
    operation = input("Choose operation(+,-,*,/): ")

    if operation == "+":
        print(num1+num2)
    elif operation == "-":
        print(num1-num2)
    elif operation == "*":
        print(num1*num2)
    elif operation == "/":
        print(num1/num2)
    else:
        print("Invalid Operation")

except ValueError:
    print("Enter Numbers Only")
except ZeroDivisionError:
    print("Cannot Divide by Zero")

finally:
    print("Operation Completed")"""

# Topic 2: Logging
# Practice 3
# Student Marks Program

"""import logging

logging.basicConfig(
    filename = "app.log",
    level=logging.ERROR
)

try:
    name = input("Enter a Name: ")
    mark = int(input("Enter your mark: "))

    if 0<= mark >=100:
        raise ValueError("The mark should be 0 to 100")
except Exception as e:
    print("Error: ", e)
    logging.error(f"Error occured: {e}")

else:
    print("Student Name: ",name)
    print("Mark", mark)

finally:
    print("Student Mark Program Conpleted")"""


# Topic 3: OOP Basics
# Practice 4

"""class employees:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(self.name)
        print(self.salary)

emp1 = employees("Johnson", 15000)
emp2 = employees("PremNath", 20000)

emp1.display()
emp2.display()"""

# Topic 5: Encapsulation
# Practice 6

"""class BankAccount:
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
     return self.__balance

account = BankAccount()

account.deposit(1000)
account.deposit(500)

print(account.get_balance())"""

# Topic 6: APIs
# Practice 7\

"""import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    data = response.json()

    print(data["name"])
    print(data["email"])
    print(data["phone"])

except Exception as e:
    print("Error: ",e)"""
