# List Comprehension

numbers=[1,2,3,4,5]

print(numbers) # [1, 2, 3, 4, 5]

doubled_numbers=[num * 2 for num in numbers]

print(doubled_numbers) # [2, 4, 6, 8, 10]

# Dictionary Comprehension

items=dict(first=1,second=2,third=3)

print(items) # {'first': 1, 'second': 2, 'third': 3}

squared_items={key:value**2 for key,value in items.items()} 

print(squared_items) # {'first': 1, 'second': 4, 'third': 9}

#--------------------

doubled_numbers={num:num for num in [1,2,3,4,5]} # Create a dict

print(doubled_numbers) # {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

#--------------------

doubled_numbers={num:num*2 for num in [1,2,3,4,5]}

print(doubled_numbers) # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

#--------------------

simple_numbers = { key: ("Even" if key % 2 == 0 else "odd") for key in [1,2,3,4,5]  }

print(simple_numbers) # {1: 'odd', 2: 'Even', 3: 'odd', 4: 'Even', 5: 'odd'}
