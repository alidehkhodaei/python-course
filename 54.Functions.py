from random import choice


# send a function to other function.

def test(num, fun):
    total = 0
    for i in range(1, num + 1):
        total += fun(i)
    return total


def square(num):
    return num * num


print(test(5, square))

# -----------------------

# Define a function to other function.

def test_2(name):
    def test_3():
        return choice(("Hi ", "Hello ", "Bye "))

    return test_3() + name


print(test_2("Ali"))

# -----------------------

# Return a fuunction

def test_33(name):
    def test_4():
        return "Hello "+name
    return test_4

t=test_33("Ali")
print(t) # <function test_33.<locals>.test_4 at 0x000001EC087A8B80>
print(t()) # Hello Ali
