class User:
    class_attribute = 0

    def __init__(self, name, family):  # This self is an instance of class. We can change name of self
        self.name = name
        self.family = family

    @classmethod  # This is decorator
    def class_method(cls):  # This cls is not an instance of class, That's this class. We can't change name of cls.
        return cls

    @classmethod
    def class_method_2(cls):
        return cls("Ali", "Ahmadi") # Create a new instance of this class

    @classmethod
    def class_method_3(cls):
        return cls.class_attribute # return class attribute


print(User.class_method())  # <class '__main__.User'>

print(User.class_method_2().name)  # Ali

print(User.class_method_3())  # 0
