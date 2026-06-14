# Practice 1 - else

#else runs only if no exception occurs

"""try:
    age = int(input("Enter a Age: "))
except ValueError:
    print("Invalid Value")
else:
    print("Your Age is: ", age)"""

#except → runs when error occurs
#else → runs when no error occurs

# Practice 2 Finally

#finally always executes.
#Whether:
#Error occurs
#No error occurs

"""try:
    num = int(input("Enter a nun: "))
except ZeroDivisionError:
    print("Cannot Divide")
finally:
    print("Program Finished")
"""
#Always runs 

#Practice 3 Multiple Exceptions
#Sometimes multiple errors can happen

"""try:
    num = int(input("Enter a number: "))
    print(10/num)
except ZeroDivisionError:
    print("Cannot Divide zero")
except ValueError:
    print("Enter Numbers Only")
"""

# Practice 4 Exception as e

"""try:
    file = open("new.txt")
except Exception as e:
    print("Error: ", e)"""
