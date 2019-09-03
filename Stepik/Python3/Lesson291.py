# lst  = [int(i) for i in input().split()]
lst = [1, 3, 5, 6, 10]

if (len(lst) > 2):
    for i in range(0, len(lst)):
        if (i == 0):
            print(lst[i - 1] + lst[i + 1])
        elif (i == len(lst) - 1):
            print(lst[i - 1] + lst[0])
        else:
            print(lst[i - 1] + lst[i + 1])
elif (len(lst) == 1):
    print(lst[0])
elif (len(lst) == 0):
    print("", end='')
elif (len(lst) == 2):
    print(lst[0] + lst[1])
