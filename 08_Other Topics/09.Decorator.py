def my_decorator(fun):
    def bye(): # Wrapper
        fun()
        print("Bye")

    return bye


def hi():
    print("Hello")


#hi_by_decorator = my_decorator(lambda:hi())
# Or
hi_by_decorator = my_decorator(hi)
hi_by_decorator()




'''
Hello
Bye
'''

#------------------------------

def my_decorator(fun):
    def bye():
        fun()
        print("Bye")

    return bye

@my_decorator
def hi():
    print("Hello")

hi()

'''
Hello
Bye
'''


#------------------------------

def my_decorator(fun):
    def bye(name):
        fun(name)
        print("Bye")

    return bye

@my_decorator
def hi(name):
    print(f"Hello {name}")

''' Syntax error because we have only one parameter.
@my_decorator
def hi(name,family):
    print(f"Hello {name} {family}")
'''

hi("Ali")

'''
Hello Ali
Bye
'''

#------------------------------

def my_decorator(fun):
    def bye(name,family):
        fun(name,family)
        print("Bye")

    return bye

@my_decorator
def hi(name,family):
    print(f"Hello {name} {family}")

hi("Ali","Ahmadi")

'''
Hello Ali Ahmadi
Bye
'''

#------------------------------

def my_decorator(fun):
    def bye(*args,**kwargs):
        fun(*args,**kwargs)
        print("Bye")

    return bye

@my_decorator
def hi(name):
    print(f"Hello {name}")

@my_decorator
def hi_2(name,family):
    print(f"Hello {name} {family}")

@my_decorator
def hi_3(name,family,age):
    print(f"Hello {name} {family} {age}")

hi("Ali")
hi_2("Ali","Ahmadi")
hi_3("Ali","Ahmadi",23)

'''
Hello Ali
Bye
Hello Ali Ahmadi
Bye
Hello Ali Ahmadi 23
Bye
'''
