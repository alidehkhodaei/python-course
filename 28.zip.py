number_1=[1,2,3,4]

number_2=[5,6,7,8]

result=zip(number_1,number_2)

print(result) # <zip object at 0x0000026E31F93700>

print(list(result)) # [(1, 5), (2, 6), (3, 7), (4, 8)]

print(list(result)) # []

#---------------------------

result=zip(number_1,number_2)

print(dict(result)) # {1: 5, 2: 6, 3: 7, 4: 8}

#---------------------------

items= [(1, 5), (2, 6), (3, 7), (4, 8)]

print(*items) # (1, 5) (2, 6) (3, 7) (4, 8)

print(list(zip(items))) # [((1, 5),), ((2, 6),), ((3, 7),), ((4, 8),)]

print(list(zip(*items))) # [(1, 2, 3, 4), (5, 6, 7, 8)]

#---------------------------

print(max((4,6)))

#---------------------------

items_1=[7,85,6]

items_2=[30,8,4]

items_3=[5,7,2]

result=zip(items_1,items_2,items_3)

print(list(result)) # [(7, 30, 5), (85, 8, 7), (6, 4, 2)]

#---------------------------

students=["Ali","Reza","Sara"]

midterm=[78,85,94]

final=[90,88,92]

final_grade=[x for x in zip(midterm,final)] # [(78, 90), (85, 88), (94, 92)]

final_grade=[max(x) for x in zip(midterm,final)] # [90, 88, 94]

# test=[max(x) for x in [1,2,3]] # Error because a list or deict must be passed (max(1),max(2) and max(3) are wrong!)

print({t[0]:max(t[1],t[2]) for t in zip(students,midterm,final)}) # {'Ali': 90, 'Reza': 88, 'Sara': 94}

#---------------------------

items=[1,2,3,4,5]

print(list(map(lambda x:x%2==0,items))) # [False, True, False, True, False]

print(list(filter(lambda x:x%2==0,items))) # [2, 4]

#---------------------------

students=["Ali","Reza","Sara"]

midterm=[78,85,94]

final=[90,88,92]

maximum=zip(students,map(lambda x:max(x),zip(midterm,final)))

print(dict(maximum)) # {'Ali': 90, 'Reza': 88, 'Sara': 94}

#---------------------------

students=["Ali","Reza","Sara"]

midterm=[78,85,94]

final=[90,88,92]

avgerage=zip(students,map(lambda x:x[0]+x[1]/2,zip(midterm,final)))

print(dict(avgerage)) # {'Ali': 123.0, 'Reza': 129.0, 'Sara': 140.0}
