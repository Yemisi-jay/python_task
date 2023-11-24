
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old")

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I am majoring in {self.major}.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and  teach {self.subject}.")

x = Person('Ade', 20)
x.introduce()

x = Student('Peter', 23,'Mathematics')
x.introduce()

x = Teacher('Mrs Betty', 45, 'English')
x.introduce()



class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        new_balance = amount + self.balance
        print(new_balance)

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        new_balance = amount + self.interest_rate + self.balance
        print(new_balance)

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, withdrawal_limit):
        super().__init__(account_number, balance)
        self.withdrawal_limit = withdrawal_limit

    def deposit(self, amount):
        new_balance = amount + self.balance
        print(new_balance)

    def withdraw(self, amount):
        new_balance = self.balance - amount
        if new_balance <= self.withdrawal_limit:
            print(new_balance)
        else:
            print ('Withdrawal limit exceeded')
            return(balance)

x = BankAccount(8123456789, 3000)
x.deposit(2000)

x = SavingsAccount(4123456789, 3000, 0.20)
x.deposit(3000)

x = CheckingAccount(3123456789, 1000, 1000)
x.deposit(1000)
x.withdraw(4000)



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        print(self.salary)

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        print(self.salary + self.bonus)

x = Employee('Martins', 50000)
x.get_salary()

x = Manager('Adeolu', 85000, 10000)
x.get_salary()
