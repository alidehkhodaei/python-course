tuple_numbers=(1,2,3,4,5,3,4,3,5) # immutable list

print(tuple_numbers[0]) # 1

print(3 in tuple_numbers) # True

tuple_numbers[1]=2 # Error because tuple is immutable.

#------------------------

new_tuple=tuple([1,2,3,4,5])

print(new_tuple) # (1, 2, 3, 4, 5)

#------------------------

locations={
(33.56,45.78):"Tehran",
(31.16,55.38):"Shiraz"
}

print(locations[(31.16,55.38)]) # Shiraz

#------------------------

for num in tuple_numbers:
    print(num)

#------------------------

print(tuple_numbers.count(3)) # 3

print(tuple_numbers.index(2)) # 1

print(tuple_numbers[2]) # 3

#------------------------

tuple_numbers=(1,2,3,4,(55,66,77))

print(tuple_numbers[4]) # (55,66,77)

print(tuple_numbers[4][2]) # 77

print(tuple_numbers[0:2]) # (1, 2)
