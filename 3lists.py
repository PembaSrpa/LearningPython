from pprint import pprint

fruits = ['Apple', 'Banana', 'Mango']
fruits2 = ['DragonFruit', 'Strawberry']
print(fruits)
print(len(fruits))
print(fruits[0])
print(fruits[-1])
print(fruits[0:2]) #all the way up to 2 but not including 2
print(fruits[:2]) #same

fruits.append('Orange')
print(fruits)
fruits.insert(0, 'Pineapple')
print(fruits)
# fruits.insert(0, fruits2)
# print(fruits) Not good [[''],'','']
fruits.extend(fruits2)
print(fruits)

fruits.remove('Banana')
fruits.pop() #removes last value
print(fruits)
popped=fruits.pop()
print(popped)

fruits.reverse()
print(fruits)

nums = [1,4,5,7,2,3,0]
nums.sort()
print(nums)

fruits.sort()
print(fruits)

nums.sort(reverse=True)
print(nums)

#without altering the original
a= sorted(nums)
print(a)

print(fruits.index('Mango'))
print('Apple' in fruits)

for item in fruits:
    print(item)
for item in enumerate(fruits, start=1):
    print(item)

fruits_str = ','.join(fruits)
print(fruits_str)
newlist= fruits_str.split(',')
print(newlist)

#lists = mutable  tuple=immutable
# use tuple when you want dont want to modify

fruitstuple = ('Apple', 'Banana', 'Mango')
#fruitstuple[0] = 'Strawberry'  cant modify causes error

#sets
fruitssets = {'Apple', 'Banana', 'Mango'} #random order
print(fruitssets) #build multiple sets to see
cs={'History', 'Math', 'Physics', 'Compsci'}
art={'History', 'Math', 'Art', 'Design'}
pprint(cs.union(art))
print(cs.intersection(art))
print(cs.difference(art))

#Empty Lists
empty_list=[]
empty_list=list()
#Empty Tuples
empty_tuple=()
empty_tuple=tuple()
#Empty Sets
empty_set={} #doesnt actually create empty set, it creates dictionary
empty_set=list() #only way
