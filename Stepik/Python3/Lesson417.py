import requests
import simplecrypt

code = requests.get(r'https://stepic.org/media/attachments/lesson/24466/encrypted.bin').content
passes = requests.get(r'https://stepic.org/media/attachments/lesson/24466/passwords.txt').content

for password in passes.split():
    try:
        c = simplecrypt.decrypt(password, code)
    except simplecrypt.DecryptionException:
        pass
    else:
        print(c.decode('utf8'))

import simplecrypt

# encrypted = open("encrypted.bin", "rb").read()
# passwords = open("passwords.txt").readlines()
#
# for p in passwords:
#     p = p.strip()
#     try:
#         s = simplecrypt.decrypt(p, encrypted)
#     except simplecrypt.DecryptionException:
#         continue
#
#     print(s.decode("utf-8"))﻿

# import simplecrypt
# with open('encrypted.bin','rb')  as inf:
#     binstr = inf.read()
# with open('passwords.txt','rb') as inf:
#     pasword = [i.decode("utf-8") for i in inf.read().split()]
#     for pas in pasword:
#         try:
#           print(simplecrypt.decrypt(pas,binstr).decode("utf-8"))
#           break
#         except:
#             continue