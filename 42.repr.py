class User:
    def __init__(self, name, family):
        self.name = name
        self.family = family


print(User("Ali", "Ahmadi")) # <__main__.User object at 0x000001A9D7145390> # Show address of instance

#--------------------

class User2:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def __repr__(self):
        return f"{self.name}  {self.family}"


print(User2("Ali", "Ahmadi")) # Ali  Ahmadi
