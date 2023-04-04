# while

password=input("Enter password")
while password!='1234':
   print("Password is not correct")
   password=input("Enter password")

# break

num=1
while(num<10):
 print(num)
 num+=1
 if(num==7):
  break

# or in for

for i in range(1,10):
 print(i)
 if(i==7):
  break
