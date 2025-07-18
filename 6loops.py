# Demonstrates for and while loops

nums = [1, 2, 3, 4, 5]

# For loop with break
for num in nums:
    if num == 3:
        print('Found it')
        break  # Stops loop when 3 is found
    print(num)

# For loop with break after printing
for num in nums:
    print(num)
    if num == 3:
        print('Found it')
        break

# For loop with continue
for num in nums:
    if num == 3:
        print('Found it')
        continue  # Skips printing 3
    print(num)

# Nested loops
for num in nums:
    for letter in 'ab':
        print(num, letter)

# Range in for loop
for i in range(1, 11):
    print(i)

# While loop
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

# Infinite loop example (commented out)
# while True:
#     print(x)
#     x += 1
