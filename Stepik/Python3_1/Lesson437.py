num = input().split()
xnum = (int(i) for i in num)
# def posit (i):
#     return i > 0
#
# pos = list(filter(posit, xnum))
# print(pos)

print(*list(filter(lambda x: x > 0, xnum)))