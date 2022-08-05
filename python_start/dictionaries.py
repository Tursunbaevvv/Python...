


""" Словари (dict) """

# Словарь - изменяемый, итерируемый. Состоят из пар:   ключ: значение. Ключами могут быть только неизменяемые типы данных(tuple, str, int, None, bool),
# а значением - любые.ключи должны быть уникальными 

import email
from email.policy import default
import imp
from optparse import Values
from re import I
import string
from traceback import print_tb
from unicodedata import name


# dict_ = {}
# passport = {"name": "Myrzabe", "last_name": "Tursunbaev", "age": 20, "gender": "M", "birthday": "19.09.2002"}

# print(passport["name"]) # "Myrzabek"
# print(passport["birthday"]) # "19.09.2002"

# dict2 = dict(name = "Myrzabek", last_name = "Tursunbaev", age = 19)

# print(dict2["last_name"])

# dict3 = dict.fromkeys(["a", "b"], 25)
# print(dict3) # {'a': 25, 'b': 25}


# dict4 = dict.fromkeys(["a", "b"]) 
# print(dict4)


# dict5 = dict([("name", "johon."), ("last_name", "Watson")])
# print(dict5["name"])


""" Методы словарей """



dict_ = {}
passport = {"name": "Myrzabek", "last_name": "Tursunbaev", "age": 20, "gender": "M", "birthday": "19.09.2002"}

# print(passport["name"]) # "Myrzabek"
# print(passport.get("name")) # "Myrzabek"
# print(passport.get("ID")) # None

# dict.get(key, None) - отдает значение указанного ключа, если нет - отдает второе указанное значение (по умолчанию None)

# print(passport.get("ID","not key!")) # not key 

# passport.setdefault(key, default ) - отдает значение указанного ключа , если его нет  - создает его со значением default(по умолчаниею - None )
# passport.setdefault("age") # 20 
# print(passport.setdefault("id"))
# print(passport) #None  {'name': 'Myrzabek', 'last_name': 'Tursunbaev', 'age': 20, 'gender': 'M', 'birthday': '19.09.2002', 'id': None}

# print(passport.setdefault("id", 123153))
# print(passport)

# passport.update({key: values}) - приниемает в себя другой словарь и обновляет исходный  словарь за счет него

# dict8 = {"name": "Malika", "age": 76, "id": 1241523, "name": "alina"} 
# # print(dict8)

# passport.update(dict8)

# print(passport)

# a = {"a": 10, "b": 20}
# a["c"] = 30 
# a["b"] = 50
# print(a) #{'a': 10, 'b': 50, 'c': 30}

dict10 = {"name": "alina", "last_name": "Serik", "age": 46}
# dict10.pop("name")
# print(dict10)

# deleted_el = dict10.pop("id", "not key! ")
# print(deleted_el)
# print(dict10)

# deleted_el = dict10.popitem()
# print(deleted_el)
# print(dict10)


# dict10.clear()
# print(dict10)


iter_dict = {"a": 10, "b": 20, "c": 241, "d": 12412}
# for i in iter_dict:
#     print(i) #keys
# for i in iter_dict:
#     print(iter_dict[i]) # values


"""keys(), values(), items()"""

# k = iter_dict.keys()
# # print(k)
# for key in k:
#     print(key)
# v = iter_dict.values()
# # print(v)
# for value in v:
#     print(value)

# i = iter_dict.items()
# # print(i)
# for key, value in i:
#     print(f"keys {key}, znachenia {value}")

cotacts = {
    "names":{
        "aidar": 1-5191951029,
        "batay": 30592-3509341,
        "igor": 39508195981898,
    }
}
# print(cotacts["names"]["igor"])
# names = cotacts ["names"]
# print(names["igor"])


# copy() - копия словаря
# cotacts_copy = cotacts.copy()

# from string import ascii_lowercase
# from string import ascii_uppercase
# a = {ascii_lowercase}
# print(a)


# alphabit = {
#     "abcdefghijklmnopqrstuvwxyz":{
#         for a in alphabit:

#     }

# from string import ascii_lowercase
# a = {}
# num = 1
# for i in ascii_lowercase:
#     a[i] = num 
#     num += 1
# print(a)




# alph = []
# for i in range(97,123):
#     alph.append(chr(i))
# # print(alph)
# doct_ = {}
# for i in alph:
#     dict_[i] = ord(i) - 96
# print(dict_)

emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
       'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
       'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
       'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
       'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
       'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
for key, value in emails.items():
    for name in value:
        print(name + "@" + key)



