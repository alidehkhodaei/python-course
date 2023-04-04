items=[1,2,3,4,5]

#-----------------------

new_items=[]

for num in items:
    new_items.append(num*2)

print(items) # [1, 2, 3, 4, 5]

print(new_items) # [2, 4, 6, 8, 10]

#----------------------

new_items=[num*2 for num in items] # Syntax list comprehension 

print(items) # [1, 2, 3, 4, 5]

print(new_items) # [2, 4, 6, 8, 10]

#----------------------

name="Ali"

names=[char for char in name]

print(names) # ['A', 'l', 'i']

#----------------------

name="Ali"

names=[char.upper() for char in name]

print(names) # ['A', 'L', 'I']

#----------------------

my_numbers=[1,2,3,4,5,6,7,8,9,10]

even=[num for num in my_numbers if num%2==0]

odd=[num for num in my_numbers if num%2!=0]

print(even) # [2, 4, 6, 8, 10]

print(odd)  # [1, 3, 5, 7, 9]

#----------------------

my_numbers=[1,2,3,4,5,6,7,8,9,10]

new_numbers=[num*2 if num%2==0 else num*3 for num in my_numbers ] # When use else, it must before for.  

# Or

# new_numbers=[]
# for num in my_numbers 
# if num%2==0:
# new_numbers.append(num*2) 
# else:
# new_numbers.append(num*3) 

print(my_numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(new_numbers) # [3, 4, 9, 8, 15, 12, 21, 16, 27, 20]
