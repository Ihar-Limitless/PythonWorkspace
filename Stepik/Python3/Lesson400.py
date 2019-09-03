a = input()
start = a[0]
a = a[1:]
count = 1
while True:
    if len(a)!=0:
        if a[0] == start:
            count+=1
            a = a[1:]
        else:
            print(str(count)+start if count>1 else start, end='')
            start = a[0]
            count = 0
    else:
        print(str(count) + start if count > 1 else start, end='')
        break


# inp = input()
# from itertools import groupby
# for k, g in groupby(inp):
# 	count = len(list(g))
# 	if count == 1:
# 		print(k, end="")
# 	else:
# 		print("{}{}".format(count, k), end="")

# s = input()
# r = ''
# n, c = 1, s[0]
# for x in s[1:]+'\n':
#     if x != c:
#         print(str(n) + c if n > 1 else c, end='')
#         n, c = 1, x
#     else:
#         n += 1