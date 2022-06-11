me={
    "name":"Ali",
    "family":"Ahmadi",
    "age":23
}
#-------------------

second={"location":"Esfahan"}

second.update(me)

print(second) # {'location': 'Esfahan', 'name': 'Ali', 'family': 'Ahmadi', 'age': 23}

#-------------------

second["name"]="Sara"

print(second) # {'location': 'Esfahan', 'name': 'Sara', 'family': 'Ahmadi', 'age': 23}

#-------------------

second["other_name"]="Sari"

print(second) # {'location': 'Esfahan', 'name': 'Sara', 'family': 'Ahmadi', 'age': 23, 'other_name': 'Sari'}

#-------------------

print(me) # {'name': 'Ali', 'family': 'Ahmadi', 'age': 23}

me.pop("name")

print(me) # {'family': 'Ahmadi', 'age': 23}

#-------------------

print(me) # {'family': 'Ahmadi', 'age': 23}

me.popitem() # delete item from last dict

print(me) # {'family': 'Ahmadi'}
