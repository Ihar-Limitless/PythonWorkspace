import re, sys

str = ['zabcz',
       'zzz',
       'zzxzz',
       'zz'
       'zxz',
       'zzxzxxz']

# [print(line.rstrip()) for line in str if re.search(r'z\w{3}z', line)]
[print(line.rstrip()) for line in str if re.search(r'z...z', line)]

# for i in str:
#        i = i.rstrip()
#        if re.search(r'z\w{3}z', i):
#               print(i)
