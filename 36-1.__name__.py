from second import sayName2 # When a module imported, all codes runned for example sayName3() is runned.

# __name__ return name module 

def sayName1():
    print(f"__name__ in first.py: {__name__}")

sayName1() # __main__ because sayName1() is here.

sayName2() # second because sayName2() imported.
