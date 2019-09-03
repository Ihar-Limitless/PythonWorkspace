n = int(input())
a = [int(x) for x in input().split()]
ans = []
for i in range(1, len(a)):
    j = i
    while j > 0 and a[j] > a[j - 1]:
        if j > 3:
            ans.append((j - 4, j))
            ans.append((j - 4, j - 1))
            ans.append((j - 4, j))
        else:
            ans.append((j + 3, j - 1))
            ans.append((j + 3, j))
            ans.append((j + 3, j - 1))
    a[j - 1], a[j] = a[j], a[j - 1]
    j -= 1

print("YES")
print(len(ans))
for (x, y) in ans:
    print(x + 1, y + 1)
