from functools import wraps

def my_decorator(func):
    def wrapper():
        func()
        print("Test")

    return wrapper


@my_decorator
def hello():
    print("Hello")


hello()
print(hello.__name__) # wrapper

# برای رفع تغییر اسم فانکشن از wrap استفااده میکنیم

#-----------------------------


def my_decorator(func):
    @wraps(func)
    def wrapper():
        func()
        print("Test")

    return wrapper

@my_decorator
def hello():
    print("Hello")


hello()
print(hello.__name__) # hello
