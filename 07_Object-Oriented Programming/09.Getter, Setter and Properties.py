class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age


me = Person("Ali", "Ahmadi", -12)
print(me.age)  # -12

me.age = 23
print(me.age)  # 23

me.age = -16
print(me.age)  # -16

# ----------------

class Person2:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    def get_age(self): # Getter
        return self._age

    def set_age(self, new_age): # Setter
        if new_age >= 0:
            self._age = new_age  # Don't have else because if age set to 23 in (__init__) and set_age(-10), 23 changed to zero.
        # else:
        #   self._age = 0


me = Person2("Ali", "Ahmadi", -12)
print(me.get_age())  # 0

me.set_age(-16)
print(me.get_age())  # 0

me.set_age(12)
print(me.get_age())  # 12

# ----------------

class Person3:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # Properties
    # me.age() -> Error / me.age -> Correct

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self._age = new_age


me = Person3("Ali", "Ahmadi", -12)
print(me.age)  # 0

me.age = -16
print(me.age)  # 0

me.age = 12

print(me.age)  # 12
