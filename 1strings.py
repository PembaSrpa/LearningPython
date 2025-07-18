# Demonstrates basic string operations in Python

message = "Hello"

a = " P's world"  # String with single quote
b = ' a"b" umm'   # String with double quotes

print(message)     # Print the string
print(a)
print(b)
print(len(message))  # Length of the string
print(a[2])          # Access character by index
print(message[0:-2]) # Slicing strings
print(message[:-2])
print(message[1:])
print(message.lower())  # Convert to lowercase
print(message.upper())  # Convert to uppercase
print(message.count("l"))  # Count occurrences of a character
print(message.find("H"))   # Find index of a character
c = a.replace("world", "code")  # Replace substring
print(c)
d = message + " +" + a           # String concatenation
print(d)
e = '{} +{}'.format(message, a)  # String formatting
print(e)
f = f'{message} +{a} hehe'       # f-string formatting
print(f)
# print(dir(message))  # Shows all string methods
# print(help(str.lower))  # Help on string lower method
