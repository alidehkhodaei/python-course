# Generator is an iterator

def count(max):
    count = 1
    while count < max:
        return count
        count += 1


print(count(5))  # 1
print(count(5))  # 1
print(count(5))  # 1

# ----------------------------

def count_2(max):  # Generator function
    count = 1
    while count < max:
        yield count
        count += 1


c2 = count_2(5)
print(next(c2))  # 1
print(next(c2))  # 2
print(next(c2))  # 3
print(next(c2))  # 4
#print(next(c2)) # Error

# Or

for item in count_2(5):
  print(item)

# ----------------------------

def my_gen():  # A simple generator function
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


g = my_gen()
print(g) # <generator object my_gen at 0x00000279F6C55E70>
print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # 3
# next(g) # Error

# Or

for item in my_gen():
    print(item)

# ----------------------------

def fib(max):
    li = []
    a, b = 0, 1
    while len(li) < max:
        li.append(b)
        a, b = b, a + b
    return li


print(fib(10)) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# for i in fib(100000000): # Memory error
#  print(i)

'''
وقتی قراره با دیتای بزرگی کار کنیم بهتره از جنراتور اسفاده کنیم
'''

# ----------------------------


def fib_2(max):  # Generator function
    x, y = 0, 1
    count = 0
    while count < max:
        yield y
        x, y = y, x + y
        count += 1

f=fib_2(10)
print(f) # <generator object fib_2 at 0x000001A4AAF16420>
print(next(f)) # 1
print(next(f)) # 1
print(next(f)) # 2
print(next(f)) # 3
print(next(f)) # 5
print(next(f)) # 8
print(next(f)) # 13
print(next(f)) # 21
print(next(f)) # 34
print(next(f)) # 55
# print(next(f)) Error

# Or

for item in fib_2(10):
    print(item)

# for i in fib_2(100000000): # Ok
#  print(i)

