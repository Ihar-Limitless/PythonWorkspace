import sys
lst = []
for i in sys.argv:
    lst.append(i)
lst.pop(0)
print(*lst)
