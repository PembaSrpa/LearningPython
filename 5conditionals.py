# Demonstrates conditional statements and boolean logic

lang = 'Python'
if True:
    print("True")
if False:
    print("False")
if lang == 'Python':
    print('Python')
if lang != 'Java':
    print('Not Java')

num = 2
if num > 1:
    print('2>1')
if num < 3:
    print('2<3')
if num >= 2:
    print('2>=2')
if num <= 2:
    print('2<=2')

# if-elif-else structure
if lang == 'Python':
    print('Python')
elif lang == 'Java':
    print('Java')
else:
    print('None')
# Python doesn't have switch-case

user = 'Admin'
logged = True
inn = False

if user == 'Admin' and logged:
    print('Admin Page')
else:
    print('Not logged in')
if inn or logged:
    print('Either way')
else:
    print('All False')
if not inn:
    print('Not logged in')
else:
    print('Logged In')

# Identity and equality
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)        # True: values are equal
print(a is b)        # False: different objects
print(id(a))
print(id(b))
c = a
print(a is c)        # True: same object
print(id(a) == id(c))
print(id(a))
print(id(c))

# False values in Python:
# False, None, 0, '', {}, [], set(), etc.
condition1 = False
condition2 = None
condition3 = 0
condition4 = ''
condition5 = {}
if condition5:
    print('True')
else:
    print('False')
