# Define the Employee class
class Employee:
    raise_amount = 1.04  # Class variable for raise amount
    num_of_emps = 0

    # Constructor to initialize the employee's attributes
    def __init__(self, first, last, pay):
        self.first = first  # First name of the employee
        self.last = last    # Last name of the employee
        # Generate email using first and last name
        self.email = f"{first.lower()}.{last.lower()}@gmail.com"
        self.pay = pay      # Salary of the employee
        
        Employee.num_of_emps += 1
        
    # Method to return the full name of the employee
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    # Method to apply raise to the employee's pay
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# Create an instance of Employee
emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Doe', 40000)

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
print(emp_1.pay)  # Output: 52000

# Change the class variable raise_amount
Employee.raise_amount = 1.05

# Change the instance variable raise_amount for emp_1
emp_1.raise_amount = 1.06

# Print the instance's raise_amount (will use instance variable)
print(emp_1.raise_amount)  # Output: 1.06

# Print the class's raise_amount
print(Employee.raise_amount)  # Output: 1.05

# Print the instance's __dict__ (attributes)
print(emp_1.__dict__)

# Print the class's __dict__ (attributes and methods)
print(Employee.__dict__)

print(Employee.num_of_emps)