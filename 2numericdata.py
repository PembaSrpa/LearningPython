# Demonstrates numeric operations and type conversions

num = 3.14
print(type(num))      # Print type of variable

# Basic arithmetic operations
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)         # Floor division
print(3 ** 2)         # Exponentiation
print(3 % 2)          # Modulus
print(3 * (3 + 2))    # Parentheses for order

# Order of Operations - PEDMAS

print(abs(-19))       # Absolute value
print(round(3.14))    # Round to nearest integer
print(round(3.15, 1)) # Round to 1 decimal place

# Comparison operators
print(3 == 2)
print(3 != 2)
print(3 > 2)
print(3 < 2)
print(3 >= 2)
print(3 <= 2)

# String addition and type casting
a = '10'
b = '10'
print(a + b)              # Concatenation
print(int(a) + int(b))    # Numeric addition after casting
