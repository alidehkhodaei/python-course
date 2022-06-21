def custom_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


items = [1, 2, 3, 4, 5, 6]
custom_for(items)

'''
1
2
3
4
5
6
'''


# --------------------

def custom_for_2(iterable, func): # We can pass a function like print or custom function.
    iterator = iter(iterable)
    while True:
        try:
            x = next(iterator)
        except StopIteration:
            break
        else:
            func(x)


items = [1, 2, 3, 4, 5, 6]
custom_for_2(items, print)
'''
1
2
3
4
5
6
'''


def square(num):
    print(num ** 2)

items = [1, 2, 3, 4, 5, 6]
custom_for_2(items, square)
'''
1
4
9
16
25
36
'''
