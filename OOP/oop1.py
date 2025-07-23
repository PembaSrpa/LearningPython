# Define the Employee class
class Employee:
    # Constructor to initialize the employee's attributes
    def __init__(self, first, last, pay):
        self.first = first  # First name of the employee
        self.last = last    # Last name of the employee
        # Generate email using first and last name
        self.email = f"{first.lower()}.{last.lower()}@gmail.com"
        self.pay = pay      # Salary of the employee
        
    # Method to return the full name of the employee
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# Create an instance of Employee
emp_1 = Employee('John', 'Doe', 50000)

# Print the email of emp_1
print(emp_1.email)

# Print the full name using the instance method
print(emp_1.fullname())

# Print the full name using the class method and passing the instance
print(Employee.fullname(emp_1))