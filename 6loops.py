nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found it')
        break # doesnt print 3, 4, 5
    print(num)

for num in nums:
    print(num)
    if num == 3:
        print('Found it')
        break # doesnt print 4, 5

for num in nums:
    if num == 3:
        print('Found it')
        continue # doesnt print 3
    print(num)

for num in nums:
    for letter in 'ab':
        print(num, letter)

for i in range(1, 11): #range(10) = 0,1,2....,9
    print(i)

x = 0
while x < 10:  #while loop which does same thing
    if x == 5:
        break
    print(x)
    x += 1

# while True: Infinite Loop
#     print(x)
#     x += 1
