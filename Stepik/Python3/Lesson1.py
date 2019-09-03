x = [1, 2, 3]
y = x
y.append(4)

s = "123"
t = s
t = t + "4"
print(t)
print(s)

print(str(x) + " " + s)

class Counter:
    pass
x = Counter()
x.count = 0
x.count+=1
print(x.count)