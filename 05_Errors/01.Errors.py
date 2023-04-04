# Syntax error

num=2
num;;

# Name error

print(name)

# Type error

print(len(2)) # int has no len()

"Ali"+[] 

# Index error

items=[1,2,3,4,5]

print(items[8])

# Value error

print(int("test"))

# Key error

person={}

print(person["name"])

# Attribute error

"Ali".test # str object has no attribute test
