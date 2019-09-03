n = int(input())
string = input().strip()
lst = ' abcdefghijklmnopqrstuvwxyz'
str = ''
for c in string:
    str += lst[(lst.index(c) + n) % len(lst)]
print('Result: "' + str + '"')