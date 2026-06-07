#Problem 1: Even or Odd

"""number = int(input("Enter a number: "))

if number %2==0 :
    print("Even")
elif number %2!=0 :
    print("odd")
else:
    print("Not found")"""


# Problem 2: Positive / Negative / Zero

"""number = int(input("Enter a Number: "))

if number == 0 :
    print("Zero")
elif number > 0 :
    print("Positive")
else:
    print("Negative")"""

#Problem 3: Largest of Two Numbers

"""num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))

if num1>num2:
    print("num1 is greater than num2")
elif num2==num1:
    print("num1 & num2  both are equal")
else:
    print("num2 is greater than num1")"""

#Problem 4: Age Category

"""age = int(input("Enter a Age: "))

if age < 18:
    print("Minor")
elif age <= 60:
    print("Adult")
else:
    print("Senior")"""

#Problem 5: Divisible Check

"""number = int(input("Enter a number: "))

if number %3 == 0 and number %5== 0 :
    print("number is divisible by 3 & 5")
elif number %3 == 0:
    print("number is divisible by 3")
elif number %5 == 0:
    print("number is divisible by 5")
else:
    print("Not divisible")"""

#Problem 6: Grade System

"""mark = int(input("Enter a Mark: "))

if mark >= 90 :
    print("Grade A")
elif mark >= 75 :
    print("Grade B")
elif mark >= 50 :
    print("Grade C")
else:
    print("fail")"""

#Problem 7: Simple Login System

username = input("Enter a Username: ")
password = input("Enter a Password: ")

if username == "Johnson" and password == "123003" :
    print("Login successfully")
else:
    print("Invalid Password and Username")