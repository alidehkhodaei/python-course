# All classes in python inheritance from object
class Person:
    def __init__(self, name, family, age, money):
        self.name = name
        self.family = family
        self.age = age
        self.money = money

    def __repr__(self): # Method overriding. This method exist in object class.
        return f"{self.name} {self.family}"

    def __len__(self): # We defined len for this class. This len is example of polymorphism.
        return self.age
    '''
    we can see that many data types such as string, list, tuple, set, 
    and dictionary can work with the len() function. However, we can 
    see that it returns specific information about specific data types.
    '''

    def __add__(self, other): # Operator overriding
        return self.age+other.age

    def __mul__(self, other):# Operator overriding
        return self.money* other.money

    def __truediv__(self, other):# Operator overriding
        return self.money / other.money

#----------------------------------------

person_1=Person("Ali","Ahmadi",28,100000)

person_2=Person("Reza","Movahed",22,250000)

print(person_1) # Ali Ahmadi
print(len(person_1)) # 28
print(person_1 + person_2) # 50
print(person_1 * person_2) # 25000000000
print(person_1 / person_2) # 0.4
