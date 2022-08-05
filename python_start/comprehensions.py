""" comprehensions (генераторы) """


# a = []
# for i in range(10):
#     a.append(i)
# print(a)

# list2 = [i for i in range(10)]
# print(list2)


# from ast import comprehension


# comprehensions - короткий способ записи циклов для создания колекций(словари, списки, множество, кортежа)

# list3 = [выражение for выражение in итерируемый_объект]


from readline import append_history_file


names = ['alina', 'namaz', 'ali', 'janat', 'ahmad', 'alinur']

# guests = []
# for name in names:
#     guests.append(name + '10')
# print(guests)

# guests1 = [name + "10" for name in names]
# print(guests1)

# guests = []
# for name in names:
#     if name[0] == "a":
#         guests.append(name)
# print(guests)

# guests1 = [name for name in names if name.startswith("a")]
# print(guests1)

# [выражение for выражение in итер_об if условие]


nums = [1, 2, 3, 4, 5, 6]
# new_nams = []
# for a in nums:
#     if a % 2 == 0:
#         new_nams.append(a + 0.3)
#     else:
#         new_nams.append(a + 0.6)
# print(new_nams)




# new_nams3 = [num + 0.3 if num % 2 == 0 else num + 0.6 for num in nums]
# print(new_nams3)

# [тернарный оператор for элемени in итер_об]

nums = [4, 3 ,7, 7, 1, 33, 32, 36, 6556]
# nums_a = []
# for i in nums:    
#     if i > 5:
#         if i % 2 == 0:
#           nums_a.append(i + 0.3)
#         else:
#           nums_a.append(i + 0.6)
# print(nums_a)


# new_a = [num + 0.6 if num % 2 !=0 else num + 0.3 for num in nums if num > 5]
# print(new_a)


lists = [[1,2,3,], [4,5,6],[7,8,9]]
# new_list = []
# for i in lists:
#     # print(i)
#     for j in i:
#         # print(j)
#         new_list.append(j)
# print(new_list)


# new_lists = [j for i in lists for j in i ]
# print(new_lists)



# list_ = [i for i in range(1,10)]

# list_new = []
# for i in range(1, 10):
#     list_new.append(i)
# print(list_new)
# print(list_)




names = ['alininig', 'namazing', 'aliing', 'janat', 'ahmad', 'alinur']





