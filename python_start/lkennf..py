""" Калькулятор """

first_nam = int(input("Введите первое число: "))
second_nam = int(input("Введите второе число: "))
operator = input("введите оператор /, //, +, -, *, **, %: ")
if operator == "+":
    print(first_nam + second_nam)
elif operator == "-":
    print(first_nam - second_nam)
elif operator == "*":
     print(first_nam * second_nam)
elif operator == "/":
    if second_nam == 0:
        print("На ноль делить нельзя!")
    else:
        print(first_nam / second_nam)
elif operator == "//":
    if second_nam == 0:
        print("На ноль делить нельзя!")
    else:
     print(first_nam // second_nam)
elif operator == "%":
    if second_nam == 0:
        print("На ноль делить нельзя!")
    else:
        print(first_nam % second_nam)
else:
    print("Такой операции не существует! ")