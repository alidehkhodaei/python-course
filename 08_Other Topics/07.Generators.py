# Generator expressions

my_generator=(num for num in range(3))  # Similar list Comprehension

print(my_generator) # <generator object <genexpr> at 0x000001F42CB35D90>
print(next(my_generator)) # 0
print(next(my_generator)) # 1
print(next(my_generator)) # 2

# Or

my_generator=(num for num in range(3))

for item in my_generator:
    print(item)

#-------------------------------------

# print(sum(num for num in range(1000000000))) # Generator expression  Ok

print(sum([num for num in range(1000000000)])) # List Comprehension  MemoryError


'''
وقتی قراره با دیتای بزرگی کار کنیم بهتره از جنراتور اسفاده کنیم
'''
