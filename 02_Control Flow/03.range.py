result=list(range(1,10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
result=list(range(0,10)) # [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
result=list(range(10)) # [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
result=list(range(0,10,2)) # [0, 2, 4, 6, 8] When step defined, start and end must defined!
result=list(range(10,0,-1)) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Printed a pattern
for num in range(1,10):
    if num%2==1:
        for star in range(1,6):
         print("*"*star)
    else:
        for star in range(5,0,-1):
         print("*"*star)

