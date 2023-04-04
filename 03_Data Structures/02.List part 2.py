# List functions

items=[1,2,3]

print(items) # [1, 2, 3]

items.append(4)

print(items) # [1, 2, 3, 4]

#--------------

other_items=[5,6]

items.extend(other_items)

print(items) # [1, 2, 3, 4, 5, 6]

#-------------

other_items=[7,8]

items.append(other_items)

print(items) # [1, 2, 3, 4, 5, 6, [7,8]]

#--------------

items.insert(1,1.5)

print(items) # [1, 1.5,2, 3, 4, 5, 6, [7,8]]

#---------------

items.insert(-1,3)

print(items) # [1, 1.5,2, 3, 4, 5, 6,3, [7,8]]

#---------------

items.clear()

print(items) # []

#---------------

items=[1,2,3,4,5]

first_item=items.pop(0)
last_item=items.pop()

print(first_item) # 1
print(last_item) # 5
print(items) # [2,3,4]

#---------------

items.pop(1)

print(items) # [2,4]

#---------------

items=["Php","Html","Css"]

items.remove("Css")

print(items) # ['Php', 'Html']

#---------------

items=["Php","Css","Html","Css"]

items.remove("Css")

print(items) # ['Php', 'Html', 'Css']

#----------------

index_php=items.index("Php")

print(index_php)

#----------------

items=["Php","Css","Html","Css","Kotlin","Css","Java"]

index_css=items.index("Css",3) # show index css index 3 and After that.
#index_css=items.index("Css",2,5) # show index css betwen index 3 and 5 if it exist.

print(f"Index css is {index_css}") # Index css is 3

#----------------

print(items.count("Css")) # 3

#----------------

items.reverse()

print(items) 

#----------------

unordered_numbers=[8,1,3,9,2,4,7,6,5]

unordered_numbers.sort()

print(unordered_numbers) 

#----------------

fruits=["Apple","Orange","Watermelon"]

new_fruits=' - '.join(fruits)

print(new_fruits) # Apple - Orange - Watermelon

#---------------- List slicing => to make copy of a list (list[start:end:step])

items=[1,2,3,4,5,6,7,8,9]

new_items=items[1:7:1]

print(new_items) # [2, 3, 4, 5, 6, 7]

#----------------

items=[1,2,3,4,5,6,7,8,9]

new_items=items[1:7:2]

print(new_items) # [2, 4, 6]

#----------------

items=[1,2,3,4,5,6,7,8,9]

new_items=items[3:]

print(new_items) # [4, 5, 6, 7, 8, 9]

#----------------

items=[1,2,3,4,5,6,7,8,9]

new_items=items[-3:]

print(new_items) # [7, 8, 9]

#----------------

items=[1,2,3,4,5,6,7,8,9]

new_items=items[0:] # or [:] (Create a copy of all items list)

print(new_items) # [1,2,3,4,5,6,7,8,9]

print(items==new_items) # True because the values ​​are the same

print(items is new_items) # False because memory locations are different

#----------------

items=[1,2,3,4,5,6,7,8,9]

new_items=items[:4] 

print(new_items) # [1, 2, 3, 4]

#----------------

items=[1,2,3,4,5,6,7,8,9]

new_items=items[::2] # start:0 end:count of list

print(new_items) # [1, 3, 5, 7, 9]

#----------------

items=[1,2,3,4,5,6,7,8,9]

new_items=items[::-1] # Reverse (start:0 end:count of list)

print(new_items) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# You can use [::-1] for reverse a string
