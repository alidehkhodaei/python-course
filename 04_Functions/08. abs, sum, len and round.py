# Len

data="Ali"

print(len(data))

# Or

print(data.__len__())

#----------------

data=[1,2,3,4,5]

print(len(data))

#----------------

data=(1,2,3)

print(len(data))

# abs (absolute value)

print(abs(5)) # 5

print(abs(-5)) # 5

# sum

numbers=[1,2,3]

print(sum(numbers)) # 6

print(sum(numbers,10)) # 16

# round

number=4.6

print(round(number)) # 5

#----------------

number=4.2

print(round(number)) # 4

#----------------

number=4.24364566

print(round(number,2)) # 4.24 (به دلیل عدد بعدی گه سه است)

#----------------

number=4.24964566

print(round(number,2)) # 4.25 (به دلیل عدد بعدی گه نه است)
