class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family


class User(Person):
    def __init__(self, name, family, email):
        super().__init__(name, family)
        # Or
        # Person.__init__(self, name, family)
        self.email = email


user = User("Ali", "Ahmadi", "test@gmail.com")
print(user.name) # Ali
print(user.family) # Ahmadi
print(user.email)  # test@gmail.com
