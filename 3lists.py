from pprint import pprint

# List operations
fruits = ['Apple', 'Banana', 'Mango']
fruits2 = ['DragonFruit', 'Strawberry']
print(fruits)
print(len(fruits))         # Length of list
print(fruits[0])           # First element
print(fruits[-1])          # Last element
print(fruits[0:2])         # Slicing
print(fruits[:2])

fruits.append('Orange')    # Add to end
print(fruits)
fruits.insert(0, 'Pineapple')  # Insert at index
print(fruits)
# fruits.insert(0, fruits2) # Would nest the list
# print(fruits)
fruits.extend(fruits2)     # Extend with another list
print(fruits)

fruits.remove('Banana')    # Remove by value
fruits.pop()               # Remove last item
print(fruits)
popped = fruits.pop()      # Remove and return last item
print(popped)

fruits.reverse()           # Reverse list
print(fruits)

nums = [1, 4, 5, 7, 2, 3, 0]
nums.sort()                # Sort list
print(nums)

fruits.sort()              # Sort alphabetically
print(fruits)

nums.sort(reverse=True)    # Sort descending
print(nums)

# Sorted returns a new list
a = sorted(nums)
print(a)

print(fruits.index('Mango'))    # Find index
print('Apple' in fruits)        # Membership test

# Looping through lists
for item in fruits:
    print(item)
for item in enumerate(fruits, start=1):
    print(item)

# String join and split
fruits_str = ','.join(fruits)
print(fruits_str)
newlist = fruits_str.split(',')
print(newlist)

# Tuples are immutable
fruitstuple = ('Apple', 'Banana', 'Mango')
# fruitstuple[0] = 'Strawberry'  # Error: can't modify

# Sets are unordered and unique
fruitssets = {'Apple', 'Banana', 'Mango'}
print(fruitssets)
cs = {'History', 'Math', 'Physics', 'Compsci'}
art = {'History', 'Math', 'Art', 'Design'}
pprint(cs.union(art))           # Union of sets
print(cs.intersection(art))     # Intersection
print(cs.difference(art))       # Difference

# Creating empty collections
empty_list = []
empty_list = list()
empty_tuple = ()
empty_tuple = tuple()
empty_set = {}      # Actually creates a dictionary
empty_set = set()   # Correct way to create empty set
