# Defined in single line
# It is similar to Function
# Anonymous function

#-----------------------

def my_function(num): return num*num

my_function2= lambda num: num*num 

print(my_function(6))

print(my_function2(6))

#-----------------------

def sum(first,second): return first+second

sum2= lambda first,second: first+second 

print(sum(6,2))

print(sum2(6,2))

#-----------------------

print(sum.__name__) # sum (return function name)

print(sum2.__name__) # <lambda>
