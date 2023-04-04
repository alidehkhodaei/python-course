me={"name":"Ali","family":"Ahmadi"}

name_exist="name" in me
email_exist="email" in me

print(name_exist) # True
print(email_exist) # False

#----------------------

ali_exist="Ali" in me.values()

print(ali_exist) # True

#----------------------

copy_me=me.copy()

print(copy_me==me) # True

print(me is copy_me) # False

#----------------------

# fromkeys: generate default value

new_user={"name":"unknown","family":"unknown","age":"unknown"}
new_user_2={}.fromkeys(["name","family","age"],"unknown") # You can use dict instead of {}
new_user_3={}.fromkeys("name","unknown") 

print(new_user)   # {'name': 'unknown', 'family': 'unknown', 'age': 'unknown'}

print(new_user_2) # {'name': 'unknown', 'family': 'unknown', 'age': 'unknown'}

print(new_user_3) # {'n': 'unknown', 'a': 'unknown', 'm': 'unknown', 'e': 'unknown'} # "name" acts like a list (list of characters)

#----------------------

print(me.get("name")) # Ali
print(me.get("email")) # None

print(me["name"]) # Ali
print(me["email"]) # KeyError

#----------------------

print(me) # {'name': 'Ali', 'family': 'Ahmadi'}

me.clear()

print(me) # {}
