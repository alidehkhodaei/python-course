class User:
    def __init__(self, name):
        self.__name = name # Name Mangling
        print("User init")

    def say_hello(self):
        return f"Hello {self._User__name} in User class"

    def say_bye(self):
        return f"Bye {self._User__name}"


class Person:
    def __init__(self, name):
        self.__name = name
        print("Person init")

    def say_hello(self):
        return f"Hello {self._Person__name} in Person class"


class Admin(Person, User):
    def __init__(self, name):
        print("Admin init")
        print(f"got name is {name}")
        User.__init__(self, "User name")
        Person.__init__(self, "Person name")


class Admin2(Person, User):
    def __init__(self, name):
        print("Admin init")
        Super().__init__(self,name) # Only __init__ of Person is runned!


#----------------------------------

person_1 = Admin("Ali")

print(person_1._User__name) # User name
print(person_1._Person__name) # Person name
print(person_1.say_hello()) # Hello Person name in Person class (because Person is first (Admin(Person, User))). (See part 47.method resolution order.py)

print(isinstance(person_1, Admin))  # True (person_1 is instance of Admin)
print(isinstance(person_1, User))  # True
print(isinstance(person_1, Person))  # True
