# Length of list

items=[1,"blue",2,"red",3,"green"]

print(len(items))

# Create a list with range

range =range(1,30)

print(list(range))

# Show last item in list

print(items[len(items)-1])

# Show item from last list with negaive index

print(items[-1])

print(items[-2])

print(items[-3])

# Check exist a item in list

is_exist_kotlin= 2 in items

print(is_exist_kotlin)

# Show all items list

for color in items:
    print(color)

#-----------------------

for color in items:
    if type(color) == str:
     print(f"the color is:{color}")
    else:
     print(f"{color} is not color")

#-----------------------

index=0

while index<len(items):
    print(items[index])
    index+=1
