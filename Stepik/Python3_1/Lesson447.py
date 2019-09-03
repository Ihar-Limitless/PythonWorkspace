import re
pattern = r'(human)'
str = ['I need to understand the human mind',
       'humanity']
for line in str:
       line = line.rstrip()
       print(re.sub(pattern,'computer', line))

# from re import sub
# from sys import stdin
# print(sub('human', 'computer',stdin.read()))