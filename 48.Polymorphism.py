# https://www.programiz.com/python-programming/polymorphism

# Polymorphism in addition operator-------------------

print(2 + 3)

print("2" + "3")

'''
we can see that a single operator + has been used to 
carry out different operations for distinct data types.
This is one of the most simple occurrences of polymorphism in Python.
'''
# Function Polymorphism in Python----------------------

print(len("Ali"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))

# Class Polymorphism in Python-------------------------

class Cat:
    def move(self):
        print("Cat moving...")


class Dog:
    def move(self):
        print("Dog moving...")


'''
dog = Dog()
dog.move()
cat = Cat()
cat.move()
'''

for animal in (dog, cat):
    animal.move()

'''
However, notice that we have not created a common superclass or linked the classes
together in any way. Even then, we can pack these two different objects into a tuple
and iterate through it using a common animal variable. It is possible due to polymorphism.
'''

# Polymorphism and Inheritance-----------------------

class IUserService: # Like interface in java / Python don't have interface.
    def get_all_users(self): raise NotImplementedError  # Or raise NotImplementedError()

    def get_user_by_id(self): raise NotImplementedError

    def create_new_user(self): raise NotImplementedError


class UserServiceBySqlServer(IUserService):
    def get_all_users(self):
        print("Get all users by sql server")

    def get_user_by_id(self):
        print("Get user by sql server")

    def create_new_user(self):
        print("Create new user by sql server")


class UserServiceByOracle(IUserService):
    def get_all_users(self):
        print("Get all users by oracle")

    def get_user_by_id(self):
        print("Get user by oracle")

    def create_new_user(self):
        print("Create new user by oracle")


userServiceBySqlServer = UserServiceBySqlServer()
userServiceBySqlServer.create_new_user()
userServiceBySqlServer.get_all_users()
userServiceBySqlServer.get_user_by_id()

userServiceByOracle = UserServiceByOracle()
userServiceByOracle.create_new_user()
userServiceByOracle.get_all_users()
userServiceByOracle.get_user_by_id()
