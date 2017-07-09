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

print("""Wellcome in Password Generator
Programm generates random password with esteblished parameters""")
while True:
    try:
        passwdLength = int(input("Enter password length: "))
        break
    except:
        print("Enter some integer")
        
if input("Do you want uppercase letters in your password? y/n ").lower() == "y":
    dictionary += uppercase
if input("Do you want integers in your password? y/n ").lower() == "y":
    dictionary += integers
if input("Do you want special symbols in your password? y/n ").lower() == "y":
    dictionary += spec

passwd = []

for i in range(passwdLength):
    passwd.append(random.choice(dictionary))

print("\nYour password is: " + "".join(passwd))
input("Copy or remember your password end hit Enter to exit")
