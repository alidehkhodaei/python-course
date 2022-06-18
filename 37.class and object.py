class Test:
    pass  # It does not do anything


print(Test())


# ---------------

class Car:
    name = None
    color = None

    def show(self):
        return self.name + " " + self.color


benz = Car()
benz.name = "Benz 2020"
benz.color = "Red"

print(benz.name)
print(benz.color)
print(benz.show())


# ---------------

class User:

    def __init__(self, user_name, user_family):
        self.user_name = user_name
        self.user_family = user_family

    def show_full_name(self):
        return self.user_name + self.user_family


ali = User("Ali", "Ahmadi")

print(ali.user_name)

print(ali.user_family)
