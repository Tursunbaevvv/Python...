""" Условные выражения """

# >
# <
# ==
#     ----> bool()
# !=
# >=
# <=

# print(20>10)
# print(13<5)
 
# print(bool(0)) # False --- нет тока
# print(bool(1)) # True  --- есть ток
# print(bool(-1)) # True --- все цифры кроме нуля выдают True

from ast import Or
from doctest import FAIL_FAST
from re import T
from unittest import result


bool("") # Folse
bool([]) # Folse
bool({}) # Folse
bool(set()) # Folse
bool(None) # Folse



""" if """

# num = 15
# if num <= 10 :
#     print("Hello worlf")


""" else """

# num = 15
# if num > 16 :
#     print("Hello worlf")
# else:
#     print("Goodbye world")

# temperature = 40
# if temperature < 20 :
#     print("cold")
# else:
#     if temperature < 30:
#         print("тепло")
#     else:
#         if temperature > 35:
#             print("жарко")


""" elif """

# temperature = 40 
# if temperature < 50:
#     print("holodno")
# elif temperature < 30:
#     print("teplo")
# elif temperature >35:
#     print("jarko")
# else:
#     print("ochen jarko")

# num = 15 
# if num <20:
#     print("ok")
#     if num > 10:
#         print("same")
# if num < 23:
#     print("good")

# mark = int(input("введите оценку от 1 до 10:::"))
# if mark == 10:
#     result = 5
# elif mark < 10:
#     result = -5
# elif mark < 5:
#     result = 3
# else:
#     result = 4
# print(result)


# if условие:
#     действие
# elif условие:
#     другое_действие
# else:
#     действие в  случае если ни одно из выше указонных условий не сработало



# in - проверка на вхождение 
# string = "Привет! Как дела?"
# if "привет" in string.lower():
#     print("cc мои поздравления :)")
# else:
#     print(";-(")

# string = "Привет! Как дела?"
# if not "привет" in string.lower():
#     print(";-(")
# else:
#     print("cc мои поздравления :)")

""" and, or, not"""

# False and False # Folse
# True and True # True
# False and True # Folse
# True and False # folse 

# age = 19
# if age > 15 and age < 18:
#     print("ok")
# else:
#     print("not ok")

False or True # True
True or False # True
False or False # False
True or True # True


# age = 19
# if age > 10 or age < 18:
#     print("ok")
# else:
#     print("not ok")

not False # True
not True # False


# print(int(False)) # 0
# print(int(True)) # 1
# True + True

# a = 10 
# print(["ok, not ok"][a > 5])




