# -*- coding: utf-8 -*-
import random

uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L',
    'M','N','O','P','Q','R','S','T','U','V', 'W', 'X','Y','Z']

lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']

spec = ['', '!', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
        '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_`',
        '{', '|', '}', '~', '"', "'"]

integers = ['1','2','3','4','5','6','7','8','9','0']

dictionary = lowercase
print("""Добро пожаловать в Password Generator
Программа геренирует случайный пароль с указанными параметрами.
Следуйте инструкциям.\n""")

while True:
    try:
        passwdLength = int(input("Введите длину пароля: "))
        break
    except:
        print("Введите любое число")
        
if input("Добавить буквы верхнего регистра в пароль? y/n ").lower() == "y":
    dictionary += uppercase
if input("Добавить числа в пароль? y/n ").lower() == "y":
    dictionary += integers
if input("Добавить специальные символы в пароль? y/n ").lower() == "y":
    dictionary += spec

passwd = []

for i in range(passwdLength):
    passwd.append(random.choice(dictionary))

print("\nВаш пароль: " + "".join(passwd))
input("Скопируйте или перепишите Ваш пароль и нажмите Enter, чтобы выйти")
