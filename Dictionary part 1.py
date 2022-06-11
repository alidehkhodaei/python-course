# Dictionary

my_dictionary={
    "name":"Ali",
    "age":23,
    "location":"Esfahan"
}

print(my_dictionary)

#--------------------

my_dictionary_2=dict( name="Ali",age=23,location="Esfahan")

print(my_dictionary_2)

#--------------------

print(my_dictionary_2["name"])

#--------------------

for key in my_dictionary_2.keys():
    print(key)
    
# name
# age
# location  

#--------------------

for item in my_dictionary_2.values():
    print(item)
    
# Ali
# 23
# Esfahan 

#--------------------

for item in my_dictionary_2.items():
    print(item)
    
# ('name', 'Ali')
# ('age', 23)
# ('location', 'Esfahan')

#--------------------

for key,value in my_dictionary_2.items():
    print(key,value)
   
# name Ali
# age 23
# location Esfahan
