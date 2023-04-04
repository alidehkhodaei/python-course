# any 
# if a item was True any return True.
# Zero is False.

items=[0,0,0,0]

print(any(items)) # False

#----------------------------

items=[0,0,0,1]

print(any(items)) # True

#----------------------------

print(any([])) # False
