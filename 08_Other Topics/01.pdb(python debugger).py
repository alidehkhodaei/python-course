# Common pdb commands
# l: Show your code
# n: Next line
# c: Continue -> Finished debugging
# p: Print

#---------------------------

#import pdb

#pdb.set_trace() # Enable debugger

#number1=int(input("Please enter a number: "))

#number2=int(input("Please enter a number: "))

#result=number1+number2

#print(result)

#---------------------------

def add_numbers(a,b,c,d):
    import pdb; pdb.set_trace()# We can define import here instead of above.
    return a+b+c+d

result=add_numbers(1,2,3,4)

print(result)
