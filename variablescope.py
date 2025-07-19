# LEGB
#Local, Enclosing, Global, Built-in
import builtins

x = 'global x'

def test():
    # global x  # This will refer to the global variable x, Now the x will be overridden, Not good to use it
    y = 'local y'
    x = 'local x'  # This will create a new local variable x
    print(y)  # Local scope
    print(x)  # Global scope

test()
# print(y)  # This will raise an error since y is not defined in the global scope
print(x)  # This will print 'global x'

def test2(z):
    x = 'local x in test2'
    print(z)  # This will print the argument passed to the function

test2('argument z')  # Calling test2 with 'argument z'
# print(z)  # This will raise an error since z is not defined in the global scope

m = min([1, 2, 3, 4, 5])  # This will raise a syntax error, should be min([1, 2, 3, 4, 5])
print(m)  # This will not be executed due to the syntax error above

# print(dir(builtins))  # This will print the built-in functions and variables

# Using built-in functions
print(len([1, 2, 3, 4, 5]))  # This will print the length of the list
print(sum([1, 2, 3, 4, 5]))  # This will print the sum of the list

def outer():
    x = 'outer x'
    
    def inner(): 
        # nonlocal x  # This will refer to the variable x in the outer function #used more often
        # x = 'inner x'  # This will modify the outer variable x #commenting this line will make it enclosing scope
        print(x)  # This will print 'inner x'
    
    inner()
    print(x)  # This will print 'inner x' since it was modified by inner()
outer()

