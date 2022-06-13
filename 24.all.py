# all: Checked True or False every item

print(all([1,2,3,4,5])) # True

print(all([0,2,3,4,5])) # False

print(all([-1,2,3,4,5])) # True

print(all([])) # True

#----------------------------

items=[1,2,3,4,5,6]

even_items=[num for num in items if num%2==0] 

print(even_items) # [2, 4, 6]

print(all(even_items)) # True

#----------------------------

even_items=[num%2==0 for num in items]

print(even_items) # [False, True, False, True, False, True]

print(all(even_items)) # False
