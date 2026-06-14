#Part 1 – Inheritance 

#Practice 1

"""class vehicle:
    def start(self):
        print("Vehicle Started")
    
class car(vehicle):
    pass

car1 = car()

car1.start()"""

#Part 2 – Child Class Own Method

"""class employee:
    def work(self):
        print("Mini Taks Completed")
class manager(employee):
    def manage(slef):
        print("Mannaging Mini Task")

ceo = manager()

ceo.work()
ceo.manage()"""

# Part 3 – Encapsulation

"""class student:
    def __init__(self,name):
        self.__name=name
student1 = student("Johnson")

print(student1.__name)"""
        

# Part 4 – Getter Method

"""class employee:
    def __init__(self,salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary

amount = employee(150000)

print(amount.get_salary())"""

#BankAccount Mini Project

class bankaccount:
    def __init__ (self):
        self.__balance = 0
    def deposit(self,amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
account = bankaccount()

account.deposit(1000)
account.deposit(500)

print(account.get_balance())
