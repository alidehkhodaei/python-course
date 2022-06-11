# 1) is and ==
number=3
if(number==3):
    print("True")
else:
    print("False")

if(number is 3):
    print("True")
else:
    print("False")

if(type(number) is int): # or type(number) == int
    print("True")
else:
    print("False")

# difference between == and is
# the == operator => values are equal
# the is operator => point to the same object (به یک آبجکت اشاره کند)

list_1=['a','b']
list_2=list_1
list_3=list(list_1) # A new list where only have list_1 items

print(list_1==list_2)
print(list_1==list_3)

print(list_1 is list_2)
print(list_1 is list_3)

# 2)Truthiness and Falsiness

# Falsiness => empty objects, zero, empty string, None

name=''

if name:
    print("Name is't empty")
else:
    print("Name is empty")
