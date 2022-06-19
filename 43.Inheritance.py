class Person:
    class_attribute = "Test value"

    def __init__(self, name, family):
        self.name = name
        self.family = family

    def show_info(self):
        return self.name + " " + self.family

    @classmethod
    def class_method(cls):
        return cls.class_attribute


class User(Person):
    pass


you = User("Hasan", "Movahed")

print(you.name)  # Hasan

print(you.class_attribute)  # Test value

print(you.class_method())  # Test value
