class A:
    def say_hello(self):
        print("class A")


class B(A):
    def say_hello(self):
        print("class B")


class C(A):
    def say_hello(self):
        print("class C")


class D(B, C):
    def say_hello(self):
        print("class D")


# Method resolution order (ترتیب اجرای متدهای با نام یکسان در بحث ارث بری چندگانه)

item=D()
item.say_hello()

# You can see method resolution order with the following codes.
# 1) print(D.mro())
# 2) print(D.__mro__)
# 3) help(D)
