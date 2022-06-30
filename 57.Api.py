import requests
# pip install requests

response=requests.get("https://jsonplaceholder.typicode.com/posts")
# data=response.text # This is a string.
data=response.json()
for item in data:
    print(item["title"])

#---------------------------

# response=requests.get("https://jsonplaceholder.typicode.com/comments?postId=1")
# Or
response=requests.get("https://jsonplaceholder.typicode.com/comments",params={'postId':1})
data=response.json()
for item in data:
    print(item['name'])
