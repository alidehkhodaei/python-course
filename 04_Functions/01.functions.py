def say_hello():
    print("Hello!")

say_hello()

#----------------------

def square_of_7():
    7**2

result=square_of_7()

print(result) # None

#----------------------

def square_of_7():
    return 7**2

result=square_of_7()

print(result) # 49

#----------------------

def sum(a,b):
    return a+b

print(sum(2,6)) # 8

#----------------------

def sum_odd_numbers(numbers):
    total=0
    for item in numbers:
        if item%2!=0:
         total+=item
    return total

print(sum_odd_numbers([1,2,3,4,5,6,7])) # 16

#----------------------

def is_even_number(num):
    if num%2==0:
        return True
    return False    

print(is_even_number(3)) # False

print(is_even_number(8)) # True

#----------------------

def exponent(num,power=2):
  return num ** power

print(exponent(2,3)) # 8

print(exponent(2)) # 4

#----------------------

def show_full_name(first,last):
    return f"{first} {last}"

print(show_full_name("Ali","Ahmadi"))

print(show_full_name(last="Ahmadi",first="Ali"))

#----------------------

def sum_all_numbers(name,*numbers):
    print(name)
    total=0
    for num in numbers:
        total+=num
    return total

print(sum_all_numbers("First",1,2)) 
# First
# 3

print(sum_all_numbers("Second",1,2,3,4)) 
# Second
# 10

print(sum_all_numbers("Third",1,2,3,4,5,6,7)) 
# Third
# 28

#----------------------

def show_user_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} value is {value}")

show_user_info(name="Ali",family="Ahmadi",age=23)

# name value is Ali
# family value is Ahmadi
# age value is 23

show_user_info(name="Ali",family="Ahmadi",age=23,email="example@gmail.com")

# name value is Ali
# family value is Ahmadi
# age value is 23
# email value is example@gmail.com

#----------------------

def display_info(a,b,*args,defPara="defalut",**kwargs):
    return [a,b,args,defPara,kwargs]

print(display_info(1,2,6,first_name="Ali",last_name="Ahmadi"))  # [1, 2, (6,), 'defalut', {'first_name': 'Ali', 'last_name': 'Ahmadi'}]

print(display_info(1,2,6,7,8,0,1,first_name="Ali",last_name="Ahmadi"))  # [1, 2, (6, 7, 8, 0, 1), 'defalut', {'first_name': 'Ali', 'last_name': 'Ahmadi'}]

#----------------------

def sum_odd_numbers(*numbers):
    print(numbers)
    total=0
    for item in numbers:
        if item%2!=0:
         total+=item
    return total

items=[1,2,3,4,5,6,7]

print(sum_odd_numbers(items))
# Error because numbers( ([1, 2, 3, 4, 5, 6, 7],) ) in ( for item in numbers:) is not a list.
# ([1, 2, 3, 4, 5, 6, 7],) 

print(sum_odd_numbers(1,2,3,4,5,6,7)) 
# 16
# (1, 2, 3, 4, 5, 6, 7)

print(sum_odd_numbers(*items)) 
# 16
# (1, 2, 3, 4, 5, 6, 7)

#----------------------

print(items) # [1,2,3,4,5,6,7]

print(*items) # 1,2,3,4,5,6,7 (Unpack)

#----------------------

def display_info(name,family):
   print(f"{name} : {family}")

items={"name":"Ali","family":"Ahmadi"}

display_info(items) # Error

display_info(*items) # name : family

display_info(**items) # Ali : Ahmadi

#----------------------

print(items) # {'name': 'Ali', 'family': 'Ahmadi'}

print(*items) # name family

print(**items) # Error (TypeError: 'name' is an invalid keyword argument for print())
