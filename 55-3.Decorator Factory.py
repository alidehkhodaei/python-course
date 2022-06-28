from functools import wraps

# Decorator Factory
'''
A decorator factory is a function that returns a decorator.
Instead of returning a function, we will return a decorator.
'''
# ارسال آرگومان به دکوراتور به این شکل است.
# پارامتر تابع اول یعنی فکتوری دکوراتور، آرگومان ورودی دکوراتور است.
# پارامتر تابع دوم یعنی اینر دکوراتور، تابع ارسالی است.
# پارامتر تابع سوم یعنی رپر، ورودی های تابع ارسالی است.

#-------------------------------

def factory_decorator(count):
    def inner_decorator(func):
        @wraps(func)
        def wrapper(name):
            if len(name) > count:
                print("An error occured")
            else:
                func(name)
        return wrapper

    return inner_decorator


@factory_decorator(5)
def show_name(name):
    print(f"Hello {name}")


show_name("Ali") # Hello Ali

show_name("Mohammad") # An error occured
