# Sort

numbers=[1,3,6,2,8,0]

print(numbers) # [1, 3, 6, 2, 8, 0]

numbers.sort()

print(numbers) # [0, 1, 2, 3, 6, 8]

#------------------------

numbers=[1,3,6,2,8,0]

print(numbers) # [1, 3, 6, 2, 8, 0]

result=sorted(numbers)

print(result) # [0, 1, 2, 3, 6, 8]

print(numbers) # [1, 3, 6, 2, 8, 0]

result=sorted(numbers,reverse=True)

print(result) # [8, 6, 3, 2, 1, 0]

# Sort a dect--------------

users=[
    {"name":"Reza","family":"Ahmadi","age":23},
    {"name":"Sara","family":"Moradi","age":28},
    {"name":"Ali","family":"Jamshidi","age":30}
    ]

print(sorted(users,key=lambda user:user["name"])) # [{'name': 'Ali', 'family': 'Jamshidi', 'age': 30}, {'name': 'Reza', 'family': 'Ahmadi', 'age': 23}, {'name': 'Sara', 'family': 'Moradi', 'age': 28}]

print(sorted(users,key=lambda user:user["age"])) # [{'name': 'Reza', 'family': 'Ahmadi', 'age': 23}, {'name': 'Sara', 'family': 'Moradi', 'age': 28}, {'name': 'Ali', 'family': 'Jamshidi', 'age': 30}]

print(sorted(users,key=lambda user:user["age"],reverse=True)) # [{'name': 'Ali', 'family': 'Jamshidi', 'age': 30}, {'name': 'Sara', 'family': 'Moradi', 'age': 28}, {'name': 'Reza', 'family': 'Ahmadi', 'age': 23}]

# max/min--------------------

items=[1,4,5,9,3]

print(max(items)) # 9

print(min(items)) # 1

#----------------------------

items=['a','b','z']

print(max(items)) # z

print(min(items)) # a

#----------------------------

name="ahmad"

print(max(name)) # m

print(min(name)) # a

#----------------------------

names=["Ahmad","Ali","Reza","Navid","Mohammad"]

print(max(names,key= lambda name:len(name))) # Mohammad

# reversed-------------------

items=[1,2,3,4,5,6]

items.reverse()

print(items) # [6, 5, 4, 3, 2, 1]

#----------------------------

items=[1,2,3,4,5,6]

print(reversed(items)) # <list_reverseiterator object at 0x000001CE5C23BE80>

print(list(reversed(items))) # [6, 5, 4, 3, 2, 1]

#----------------------------

result=""

print(result.join(list(reversed("Hello")))) 
 
#----------------------------

for i in reversed(range(0,10)):
    print(i)
