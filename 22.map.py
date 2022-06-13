# map
items=[1,2,3,4,5]

doubled_items=map(lambda x:x*2,items) # First parameter take a function.

print(doubled_items) # <map object at 0x000002C4A276B100>

print(list(doubled_items)) # [2, 4, 6, 8, 10]

print(list(doubled_items)) # []  برای بار دوم که به دیتا استارکچر دیگه مثل لیست تبدیل میشه دیگه آیتمی درونش قرار ندارد.

#-----------------------

names=["ali","reza","hasan"]

upper_names = map(lambda name:name.upper() ,names)

print(list(upper_names)) # ['ALI', 'REZA', 'HASAN']

#-----------------------

peopel=[
    {"name":"Reza","family":"Ahmadi","age":23},
    {"name":"Sara","family":"Moradi","age":25},
    {"name":"Ali","family":"Jamshidi","age":33}
]

families = map(lambda person:person["family"] ,peopel)

print(list(families)) # ['Ahmadi', 'Moradi', 'Jamshidi']

#-----------------------

families2=[]

for person in peopel:
    families2.append(person["family"])

print(families2) # ['Ahmadi', 'Moradi', 'Jamshidi']
