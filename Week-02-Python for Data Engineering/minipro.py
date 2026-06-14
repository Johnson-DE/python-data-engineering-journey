import logging

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR
)

class employees:
    def __init__(self, name, salary):
        self.name=name
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def display_details(self):
        print("Employee Name: ", self.name)
        print("Salary: ", self.__salary)
try:
    name = input("Enter Your Name: ")
    salary = int(input("Enter Salary: "))
    if salary<0:
        raise ValueError("Salary does not be an negative")
    emp1 = employees(name, salary)
    emp1.display_details()
except Exception as e:
    print("Error: ",e)
    logging.error(f"Error: {e}")
finally:
    print("Program Completed")

