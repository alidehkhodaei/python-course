# _name  -> Similar to private in Java
# __name -> Name mangling (When two items have similar name in child and parent class (To avoid conflict))
# __name__ -> For naming special function or variable similar __init__ or __name__

# -----------------------------

class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password
        self.__message = "I love python"


me = User("Ali", "123")

# -----------------------------

print(me.username)  # Ali
print(me._password)  # printed 123 (Available but should not be used because it is private).

# -----------------------------

# The dir() function returns all properties and methods
# of the specified object, without the values.
# This function will return all the properties and
# methods, even built-in properties which are default for all object.

print(dir(me))  # Showed '_User__message' name for __message

# __message name changed to _User__message

# -----------------------------

print(me._User__message)  # I love python
print(me.__message)  # AttributeError: 'User' object has no attribute '__message'
