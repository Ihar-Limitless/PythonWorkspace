str = input()
str2 = input()
count = True
while True:
    if (str.count(str2) != 0):
        print(str.find(str2), end = " ")
        str = str.replace(str2, ("_"+str2[1:]),1)
        count = False
    else:
        if(count == True):
            print('-1')
        break

# a, b = input(), input()
# print(" ".join(map(str,[i for i in range(len(a)) if a[i:].startswith(b)])) if b in a else "-1")