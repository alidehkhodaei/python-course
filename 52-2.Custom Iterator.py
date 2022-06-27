class User:
    active_users = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        user_dic = {"name": name, "age": age}
        User.active_users.append(user_dic)
        self.index = 0

    def log_out(self):
        current_user = list(filter(lambda user: user['name'] == self.name, User.active_users))[0]
        User.active_users.remove(current_user)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(User.active_users):
            person = User.active_users[self.index]
            self.index += 1
            return person
        raise StopIteration


me = User("Ali", 24)
reza = User("Reza", 29)
hasan = User("Hasan", 21)
sara = User("Sara", 20)
sara.log_out()

for p in me:
    print(p)

'''
یک کلاسی را برای اینکه ایتریبل کنیم باید متدهای ایتر و نکست پیاده سازی شده باشند.

__iter__
آبجکت را ایتریبل میکند

__next__
آبجکت را ایتریتور میکند

'''
