import re
# name2 = name.split(' ')
# lst = []
# for i in name2:
#     if (i != ''):
#         lst.append(i)
# for i in range(0, len(lst)-1):
#    print(lst[i],end = '')
#    print('_', end = '')
# print(lst[len(lst)-1])


print(re.sub('[ ]+', '_', input()))