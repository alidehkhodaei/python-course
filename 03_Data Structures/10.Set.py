numbers={1,2,3,4,2,2,2,1,6}

print(numbers) # {1, 2, 3, 4, 6}

# مجموعه ها ترتیب خاصی ندارند و شامل اعداد تکراری هم نیستند

#--------------------

print(numbers[0]) # Error

print(4 in numbers) # True

#--------------------

for item in numbers:
    print(item)

#--------------------

courses=["a","b","c"]

courses_set=set(courses)

print(courses_set) # {'a', 'c', 'b'}

#--------------------

courses_set={"a","b","c"}

courses=list(courses_set)

print(courses) # ['a', 'c', 'b']

#--------------------

items={1,2,3,4,5,6,7}

items.add(4)

print(items) # {1, 2, 3, 4, 5, 6, 7}

#--------------------

items={1,2,3,4,5,6,7}

items.remove(4)

print(items) # {1, 2, 3, 5, 6, 7}

#--------------------

items={1,2,3,4}

items.remove(8) # Error because 8 don't exist.

items.discard(8) # remove item but if 8 don't exist don't show error

#--------------------

copy_items=items.copy()

print(copy_items) # {1, 2, 3, 4}

print(items==copy_items) # True

print(items is copy_items) # False

#--------------------

class_a={"Ali","Milad","Mohammad","Sara"}

class_b ={"Mohammad","Ahmad","Reza","Ali"}

print(class_a | class_b) # اجتماع {'Ali', 'Sara', 'Reza', 'Milad', 'Ahmad', 'Mohammad'}

print(class_a & class_b) # اشتراک {'Ali', 'Mohammad'}

#--------------------

new_set={x**2 for x in range(10)}

print(new_set) # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

#--------------------

new_set={char for char in "Hello World!"}

print(new_set) # {'e', ' ', 'r', 'o', 'l', 'd', '!', 'W', 'H'}

#--------------------

items.clear()

print(items) # set() (Empty set)
