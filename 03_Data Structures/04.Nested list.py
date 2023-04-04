list= [[1,2,3],[4,5,6]]

index=list[1][2]

print(index) # 6

#--------------------

for li in list:
    for num in li:
        print(num)
#1
#2
#3
#4
#5
#6

#--------------------

copy_list= [print(li) for li in list]

# [1, 2, 3]
# [4, 5, 6]

#--------------------

copy_list= [ [print(l) for l in li] for li in list]

#1
#2
#3
#4
#5
#6

#--------------------

generated_list=[num for num in range(1,4)]

generated_nested_list=[ [new_num for new_num in range(1,4)] for num in range(1,4)]

print(generated_list) # [1, 2, 3]

print(generated_nested_list) # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

#--------------------

generated_nested_list=[ ['X' if new_num%2==0 else 'Y' for new_num in range(1,4)] for num in range(1,4)]

print(generated_nested_list) # [['Y', 'X', 'Y'], ['Y', 'X', 'Y'], ['Y', 'X', 'Y']]
