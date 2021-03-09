import sys
import pyperclip
from random import choice

if len(sys.argv) != 2:
    print('Incorrect Usage; Try: python password.py website.com')
    sys.exit()

text = open('pass_text.txt', 'r+')
lst = text.readlines()
for i in range(len(lst)):
    entry = lst[i][:-1]
    lst[i]=entry
passwords = {}
for i in range(0, len(lst), 3):
    passwords[lst[i]] = lst[i+1]

web = sys.argv[1]

while True:
    if web in passwords.keys():
        pyperclip.copy(passwords[web])
        print('Copied!')
        sys.exit()
    else:
        print('Not in dictionary; check spelling.')
        inp = input('Enter website again or type "new": ')
        if inp == 'new':
            break
        else:
            web = inp

upper = 'ABCDEFGHIJKLMNOPQURSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
symbols = '!@#$%^&*()<>?/~`;:'
lst = [upper, lower, numbers, symbols]
password = ''
while True:
    for _ in range(12):
        password += choice(choice(lst))
    for st in lst:
        for i in password:
            if i in st:
                break
        else:
            break
    break

text.writelines(['\n', web+'\n', password+'\n'])
pyperclip.copy(password)
print('Saved and copied!')