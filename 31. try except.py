try:
    print(num) # num is not defined
except:
    print("An error occured!")

#---------------------

def get(d,key):
    try:
      return d[key]
    except:
      return None # Or return "no key found"


person={
"name":"Ali",
"family":"Ahmadi"
}

print(get(person,"age")) # None

#---------------------

# We can define some errors in except

def get(d,key):
    try:
      return d[key]
    except KeyError:
      return "no key found" 
    except ValueError:
      return "index error" 
           
#---------------------

try:
    num=int(input("Please enter a number: "))
except:
    print("that is not a number!")
else:
    print("this is else section") # When except section don't run
finally:
    print("this is finally section")

#---------------------

try:
    num=int(input("Please enter a number: "))
except ValueError as error:
    print(error)
    print("that is not a number!")
