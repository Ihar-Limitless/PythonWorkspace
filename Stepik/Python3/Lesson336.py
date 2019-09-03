num = int(input())
lst = []
for i in range(1, num + 1):
    for j in range(i, 0, -1):
        if (len(lst) < num):
            lst.append(i)
        else:
            break
print(' '.join(str(i) for i in lst))

# ______
# from math import *
# for n in range (int(input())):
#     print (floor ((sqrt(8 * (n + 1)) + 1) / 2), end=' ')
# ______
# n = int(input())
# print(" ".join(map(str,[y for x in range(1,n+1) for y in [x]*x][0:n])))
