str = input()
count = '1'
flag = True
tmp = ''
while len(str)!=0:
    if str[0].isdigit():
        if(count == '1'):
            if flag == True:
                count = str[0]
                flag = False
            else:
                count+=str[0]
        else:
            count+=str[0]
    else:
        print(int(count)*str[0],end='')
        count = '1'
        flag = True
    str = str[1:]

# from re import sub
# print(sub(r'(\d+)(\w)', lambda m: m.group(2) * int(m.group(1)), input()))

# ______________________

# s = input()
# n = ''
# for i in range(len(s)):
#   if s[i].isdecimal():
#     n += s[i]
#   else:
#     print(s[i]*(int(n) if n else 1), end='')
#     n = ''

# ______________________
# import re
# def repl(mObj):
#     el = mObj.group(0)
#     return str(el[-1:])*int(el[:-1])
#
# print(re.sub('(\d+[a-zA-Z])', repl ,input()))