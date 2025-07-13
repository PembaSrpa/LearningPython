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

if lang == 'Python':
    print('Python')
elif lang == 'Java':
    print('Java')
else:
    print('None')
#python doesnt have switch.. elif is enough

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

a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b) # False because id is different(different object in memory)
print(id(a))
print(id(b))
c = a
print(a is c) #True because same object in memory
print(id(a) == id(c)) #basically the same
print(id(a))
print(id(c))

#False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. Eg. '', {}, []
    # Any empty mapping. Eg. {}
condition1 = False
condition2 = None
condition3 = 0
condition4 = ''
condition5 = {}
# All above is False
if condition5:
    print('True')
else:
    print('False')
