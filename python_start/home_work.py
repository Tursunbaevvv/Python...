# """ Калькулятор """

# first_nam = int(input("Введите первое число: "))
# second_nam = int(input("Введите второе число: "))
# operator = input("введите оператор /, //, +, -, *, **, %: ")
# if operator == "+":
#     print(first_nam + second_nam)
# elif operator == "-":
#     print(first_nam - second_nam)
# elif operator == "*":
#      print(first_nam * second_nam)
# elif operator == "/":
#     if second_nam == 0:
#         print("На ноль делить нельзя!")
#     else:
#         print(first_nam / second_nam)
# elif operator == "//":
#     if second_nam == 0:
#         print("На ноль делить нельзя!")
#     else:
#      print(first_nam // second_nam)
# elif operator == "%":
#     if second_nam == 0:
#         print("На ноль делить нельзя!")
#     else:
#         print(first_nam % second_nam)
# else:
#     print("Такой операции не существует! ")



# first_nam = input("Введите первое число: ")
# second_nam = input("Введите второе число: ")
# operator = input("введите оператор /, //, +, -, *, **, %: ")

# if "." in first_nam:
#     first_nam = float(first_nam)
# else:
#     first_nam = int(first_nam)
# if "." in second_nam:
#     second_nam =float(second_nam)
# else:
#     second_nam = int(second_nam)

# print(type(first_nam))
# print(type(second_nam))



""" Task number 1 """
# number = int(input())

# if number > 0:
#     print(True)
# else:
#     print(False)

""" Task number 2 """

# string = (input())
# if len(string) > 5:
#     print("True")
# else:
#     print("False")


""" Task number 3 """

# mark = int(input())
# if mark >= 90:
#     print("Отлично,Ваша оценка 5!")
# elif mark >= 80:
#     print("Здорово, Ваша оценка 4!")
# elif mark >= 70:
#     print("Хорошо, Ваша оценка 3!")
# elif mark >= 60:
#     print("Вам стоит подучить материал")
# else:
#     print("Вы не сдали экзамен")



""" Task number 4 """

# number = int(input( ))
# if number < 0:
#     print("negative")
# elif number > 0:
#     print("positive")
# else:
#     print("zero")

""" Task number 5 """


# x = 8
# y = 6

# if x > y:
#     print(y)
# else:
#     print(x)




""" Task number 6 """


"""# num = -4 #

# if num % 2 == 0 and num > 0: 
#     print('число положительное, четное') 
# else: 
#     print('число 0, отрицательное, либо не четное') 
"""

# x = int(input('Введите число: '))
# y = int(input('Введите число: '))
# z = int(input('Введите число: '))
# if x < y and x < z:
#     print(x)
# elif y < x and y < z:
#     print(y)
# else:
#     print(z)


""" Task number 7 """


# x = int(input('Введите число: '))
# y = int(input('Введите число: '))
# z = int(input('Введите число: '))
# if x == y and y == z:
#     print(input('Совпадений 3!: '))
# elif x == y or y == z or z == x:
#     print('Совпадений 2!: ')
# else:
#     print('Совпадений нет!: ')


""" Task number 8 """

x = int(input())
y = int(input())

if x % y == 0:
    print('x делится на y')
    print('Частное: ' + str(x // y))
else:
    print('x не делится на y')
    print('Частное: ' + str(x // y))
    print('Остаток: ' + str(x % y))

    