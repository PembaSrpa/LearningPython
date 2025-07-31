# Define the Employee class
class Employee:
    raise_amount = 1.04  # Class variable for raise amount
    num_of_emps = 0      # Class variable to track number of employees

    # Constructor to initialize the employee's attributes
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first.lower()}.{last.lower()}@gmail.com"
        self.pay = pay
        Employee.num_of_emps += 1

    # Method to return the full name of the employee
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Method to apply raise to the employee's pay
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Class method to set the raise amount for all employees
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # Alternative constructor to create Employee from a string
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

    # Static method to check if a given day is a workday
    @staticmethod
    def is_workday(day):
        return day.weekday() < 5  # 0-4 are weekdays
    
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"
    # Example usage of the Employee class
    
    def __str__(self):
        return f"{self.fullname()} - {self.email} - {self.pay}"
    # Example usage of the Employee class
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())


# Create instances of Employee
emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Doe', 40000)

# Set class variable raise amount
Employee.set_raise_amt(1.05)

# Print the email of emp_1
print(emp_1.email)  # Output: john.doe@gmail.com

# Print the full name using the instance method
print(emp_1.fullname())  # Output: John Doe

# Print the full name using the class method and passing the instance
print(Employee.fullname(emp_1))  # Output: John Doe

# Print the current pay
print(emp_1.pay)  # Output: 50000

# Apply raise and print the new pay
emp_1.apply_raise()
print(emp_1.pay)  # Output: 52500

# Print the class's raise_amount
# print(Employee.raise_amount)  # Output: 1.05

# Print the instance's raise_amount (will use class variable if not set on instance)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# Set raise amount again and print to show effect
Employee.set_raise_amt(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Create new Employee from string
emp_str_1 = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

# Use static method to check if a date is a workday
import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, p_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.p_lang = p_lang

dev_1 = Developer('Bob', 'Brown', 70000, 'Python')
dev_2 = Employee('Alice', 'Smith', 60000)

# print((help(Developer)))
print(dev_1.email)
print(dev_1.p_lang)
print(dev_2.email)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees 
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print('--->', emp.fullname())
            
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Developer))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

print(emp_1)
print(repr(emp_1))
print(emp_1.__repr__())#same
print(str(emp_1))

print(int.__add__(1,2))
print(str.__add__('a','b'))

print(emp_1 + emp_2) # adds salary

print(len(emp_1))