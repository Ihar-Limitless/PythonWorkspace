n = int(input())
for i in range(0, n+1):
    num = i
    s = 0
    while True:
        print("num = ", num)
        if num // 10 == 0:
            break
        else:
            s+=num % 10
            num = num //10
    print(s)