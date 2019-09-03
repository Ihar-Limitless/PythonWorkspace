lst = []
i = 0
s = ''
count = 0

with open('file.txt', 'r') as fo:
    fopen = fo.readline().strip()
    while i < len(fopen):
        if (fopen[i].isdigit() == False):
            lst.append(fopen[i])
            count = 0
        elif (fopen[i].isdigit() and count == 0):
            lst.append(fopen[i])
            count = 1
        else:
            lst[len(lst) - 1] += fopen[i]
        i += 1

with open('file2.txt', 'w') as fop:
    for i in range(0, len(lst)):
        if (i % 2 == 0):
            s = lst[i]
        else:
            fop.write(s * int(lst[i]))
