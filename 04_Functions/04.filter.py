# filter

items=[1,2,3,4,5,6]

even_items=filter(lambda x:x%2==0,items)

print(even_items) # <filter object at 0x0000020B3F56B130>

print(list(even_items)) # [2, 4, 6]

#-----------------------

users=[
{"name":"Reza","shop_cart":[]},
{"name":"Ali","shop_cart":["Java","Kotlin"]},
{"name":"Ahmad","shop_cart":[]}
]

empty_shop_cart= filter(lambda item: len(item["shop_cart"])==0,users)

print(list(empty_shop_cart)) # [{'name': 'Reza', 'shop_cart': []}, {'name': 'Ahmad', 'shop_cart': []}]

#-----------------------

empty_shop_cart= filter(lambda item: item["shop_cart"],users) #  item["shop_cart"] return items where is't empty.

print(list(empty_shop_cart)) # [{'name': 'Ali', 'shop_cart': ['Java', 'Kotlin']}]

#-----------------------

empty_shop_cart= filter(lambda item: not item["shop_cart"],users) 

print(list(empty_shop_cart)) # [{'name': 'Reza', 'shop_cart': []}, {'name': 'Ahmad', 'shop_cart': []}]

#-----------------------

empty_shop_cart= list(filter(lambda item: not item["shop_cart"],users))

result=list(map(lambda name: name["name"], empty_shop_cart))

print(result)  # ['Reza', 'Ahmad']

#-----------Or-------------

result=list(map(lambda name: name["name"],
filter(lambda item: not item["shop_cart"],users)))

print(result)  # ['Reza', 'Ahmad']

#-----------Or-------------

result=[user["name"] for user in users if len(user["shop_cart"])==0]

print(result)  # ['Reza', 'Ahmad']
