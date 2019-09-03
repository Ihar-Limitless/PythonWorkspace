lst = []
dct = {}
max = 0
k_max = ''
with open('file_2.txt', 'r') as fo:
    for line in fo.readlines():
        lst = line.strip().lower().split(' ')
        for i in lst:
            print(i)
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1

    for key, vol in dct.items():
        if (vol >= max):
            max = vol
            k_max = key
    print(k_max,max)

    # with open('file2.txt', 'w') as fop:
    #     for i in range(0, len(lst)):
    #         if (i % 2 == 0):
    #             s = lst[i]
    #         else:
    #             fop.write(s * int(lst[i]))
