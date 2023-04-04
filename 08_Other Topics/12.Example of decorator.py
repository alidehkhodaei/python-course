from time import time

start_time=time()
sum([num for num in range(20000000)])
end_time=time()

print(end_time-start_time)

#-------------------------------

# We imploment above code with decorator.

def my_decorator(func):
    def wrapper(*args,**kwargs):
        start_time = time()
        func(*args,**kwargs)
        end_time = time()
        print(f"Time Elapsed: {end_time-start_time}")
    return wrapper

@my_decorator
def sum_nums_list_comprehension(text):
 sum([num for num in range(20000000)])
 print(text)

@my_decorator
def sum_nums_generator_expression():
     sum(num for num in range(20000000))


sum_nums_list_comprehension("Finish!")
sum_nums_generator_expression()
