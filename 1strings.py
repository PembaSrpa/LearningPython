message = "Hello"

a=" P's world"

b=' a"b" umm'

print(message)
print(a)
print(b)
print(len(message))
print(a[2])
print(message[0:-2])
print(message[:-2])
print(message[1:])
print(message.lower())
print(message.upper())
print(message.count("l"))
print(message.find("H"))
c=a.replace("world","code")
print(c)
d= message + " +" + a
print(d)
e='{} +{}'.format(message,a)
print(e)
f = f'{message} +{a} hehe'
print(f)
# print(dir(message)) shows all the methods
# print(help(str.lower))
