li = [9, 1, 3, 5, 7, 4, 2]
s_li = sorted(li)
# s_li = li.sort() #this prints none
print('Sorted: \t',s_li)
# li.sort() this also sorts the original
print('Original: \t',li)

tup = [9, 1, 3, 5, 7, 4, 2]
# tup.sort() error
s_tup = sorted(tup)
print('Tuple: \t',s_tup)

di = {'name':'James', 'job':'dev', 'age':None}
s_di = sorted(di)
print('Dict:  \t',s_di)

li2 = [-6, -5, -4, 1, 2, 3]
s_li2 = sorted(li2, key=abs)
print('Abs: \t', s_li2)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)
    
e1 = Employee('Carl', 32, 7081664)
e2 = Employee('James', 28, 4351533)
e3 = Employee('jessie', 26, 6567664)
employees = [e1,e2,e3]
# s_employees = sorted(employees) unorderable types
#creating custom function to sort
def e_sort(emp):
    return emp.name
s_employees = sorted(employees, key=e_sort)
#or just use lambda
s_employees2 = sorted(employees, key=lambda e: e.salary)
print('Employees: \t',s_employees)
print('Salaries: \t',s_employees2)
#or you can import attregator and pass it as key
from operator import attrgetter
s_employees3 = sorted(employees, key=attrgetter('age'))
print('Age:\t',s_employees3)
