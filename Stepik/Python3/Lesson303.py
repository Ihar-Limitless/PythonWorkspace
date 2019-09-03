n = int(input())
dic = {}

def f(x):
    return x*1000

for i in range(0, n):
    x = int(input())
    if x in dic:
        print((dic[x]))
    else:
        dic[x] = f(x)
        print((dic[x]))

print(dic)