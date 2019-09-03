a, b = (int(i) for i in input().split())
lst = []

for i in range(a, b + 1):
    if (i % 3 == 0):
        lst.append(i)
print((sum(lst)/len(lst)))
