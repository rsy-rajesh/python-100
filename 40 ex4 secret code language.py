# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode


import os
from cryptography.fernet import Fernet
import random
import string
print(
    'if anyone need computer virus code please comment me i will provide reple link!\n')
lst = os.listdir()
key = Fernet.generate_key()


def fileencryption(filename):
    with open('thekey.key', 'wb') as f:
        content = f.write(key)
    with open(filename, 'rb') as thefile:
        filecontent = thefile.read()
        encrypt_contents = Fernet(key).encrypt(filecontent)
        with open(filename, 'wb') as f:
            f.write(encrypt_contents)


def filedcryption(filename):
    with open('thekey.key', 'rb') as k:
        key1 = k.read()
    with open(filename, 'rb') as f:
        content = f.read()
    dcrypt_content = Fernet(key1).decrypt(content)
    with open(filename, 'wb') as ff:
        ff.write(dcrypt_content)


def code_word(user1, key):
    b = user1.split()
    lst = []
    for i in b:
        if (len(i) < 3):
            a = i[::-1]
            lst.append(a)
        else:
            code = i[1:] + i[0]
            code1 = ''.join(random.choices(
                string.ascii_lowercase, k=key)) + code + ''.join(
                random.choices(string.ascii_lowercase, k=key))
            lst.append(code1)
    a = ' '.join(lst)
    return a


def dcode_word(user, key):
    b = user.split()
    lst = []
    for i in b:
        if (len(i) < 3):
            code = i[::-1]
            lst.append(code)
        else:
            code2 = i[key:-key]
            try:
                code1 = code2[-1] + code2[0:-1]
            except IndexError:
                print('Your encryption key is greater than message:')
            lst.append(code1)
    a = ' '.join(lst)
    return a


while True:
    u = input(
        'Enter Code or Decode or Quit for textfile enter(en) encryption enter (de) decryption!:\n'
    )
    if (u.lower() == "code"):
        user1 = input('Enter your message:')
        try:
            user2 = int(input('Enter your key!:'))
        except Exception as e:
            pass
        try:
            print(code_word(user1, user2))
        except Exception as e:
            print('Please enter only Digits for encryption:')
    elif (u.lower() == "decode"):
        user1 = input('Enter Your message:')
        try:
            key = int(input('Enter your key for Dcrypting:'))
            if (key > len(user1)):
                print('Your Decryption key is greater than message:')
            else:
                print(dcode_word(user1, key))
        except Exception as e:
            print('Please enter only Digits for Decryption:')
    elif (u.lower() == 'en'):
        textfile = input('Enter your text file name with .txt!')
        if (textfile.endswith('.txt')):
            textfile1 = textfile + '.txt'
        try:
            fileencryption(textfile1)
        except Exception as e:
            print('File Not found!')
    elif (u.lower() == 'de'):
        textfile = input('Enter your text file name with .txt!')
        if (not textfile.endswith('.txt')):
            textfile1 = textfile + '.txt'
        try:
            filedcryption(textfile1)
        except Exception as e:
            print('File Not found!')
    elif (u.lower() == 'quit'):
        break
    else:
        print('Please enter vaild detail:')
