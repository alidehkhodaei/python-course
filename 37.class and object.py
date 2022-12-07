class Test:
    pass  # It does not do anything


print(Test())

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
