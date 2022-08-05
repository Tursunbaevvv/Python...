# first_num = int(input('Введите первое число: '))
# second_num = int(input('Введите второе число: '))
# operator = input('введите оператор /, //, +, -, *, **, %: ')
# if operator == '+':
#     print(first_num + second_num)
# elif operator == '-':
#     print(first_num - second_num)
# elif operator == '*':
#     print(first_num * second_num)
# elif operator == '**':
#     print(first_num ** second_num)
# elif operator == '%':
#     if second_num == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(first_num % second_num)
# elif operator == '//':
#     if second_num == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(first_num // second_num)
# elif operator == '/':
#     if second_num == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(first_num / second_num)
# else:
#     print('Такой операции не существует!')


# first_num = input('Введите первое число: ')
# second_num = input('Введите второе число: ')
# operator = input('введите оператор /, //, +, -, *, **, %: ')

# if '.' in first_num:
#     first_num = float(first_num)
# else:
#     first_num = int(first_num)
# if '.' in second_num:
#     second_num = float(second_num)
# else:
#     second_num = int(second_num)

# print(type(first_num))
# print(type(second_num))



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



""" bool expressions """










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

# x = int(input())
# y = int(input())

# if x % y == 0:
#     print('x делится на y')
#     print('Частное: ' + str(x // y))
# else:
#     print('x не делится на y')
#     print('Частное: ' + str(x // y))
#     print('Остаток: ' + str(x % y))

    
""" Task number 9 """

# year = int(input())

# result = (
#     'YES' if year % 4 == 0 and 
#     year % 100 != 0 or 
#     year % 400 == 0 else 'NO'
# )

# print(result)







# 7//3 + 7//-3


# s = '\nabc\n'
# s.split('\n')
# print(s)

# from cupshelpers import Printer


# xx = 15 
# if True:
#     xx = 20
# # print(xx)

# for i in "abcd"[::-1]:
#     print(i)


# num = int(input())
# whail True:


#     if chr(num).isalpha():
#         print(f'Это буква "{chr(num)}"')
#     else:
#         print(f'Это не буква,асимвол "{chr(num)}"')

# name_of_list = ['Helloworld!']

# length = len(name_of_list[0]) + 1
# string = name_of_list[0]
# string = string[length // 2:] + string[:length // 2]
# result = list(string)

# print(result)


# name_of_list = [""]

# length =  len(name_of_list[0]) + 1 
# string = name_of_list[0]
# string = string[length // 2:] + string[: length // 2]
# result = list(string)

# print(result)




# elif len(string[0]) % 1 == 0:
#     new_list1 = list(string)
# print(new_list1, new_list)

    
"""
Создать три числа в списке list_.
Вывести на экран yes, если среди них есть одинаковые, иначе вывести ERROR.
Например, для списка [1, 1, 3], вывод будет:

yes 
а для списка [1, 2, 3]:

ERROR """

# list = [1, 2, 230, 123, 1, 2]

# num = [1, 142, 5, 1, 5, 12]
# num1 = [2, 4, 1, 142, 12]
# num3 = num == num1 
# for i in num3:
#     if num != num1:
#         result = []
    





"""  
Создайте словарь, ключами которого являются буквы английского алфавита,
 а значениями – соответствующие им порядковые номера в алфавите.
  Для удобства можете воспользоваться модулем string
"""


list_ []