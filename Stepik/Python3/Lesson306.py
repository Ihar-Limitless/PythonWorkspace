lst = []
a_val1 = 0.0
a_val2 = 0.0
a_val3 = 0.0
with open('file_2.txt', 'r') as fo:
    for line in fo.readlines():
        lst.append(line.strip().split(';'))

for a_val in lst:
    f = round(((float(a_val[1])+float(a_val[2])+float(a_val[3]))/3),9)
    print('{:.09f}'.format(f))
    a_val1+=round(float(a_val[1]),9)
    a_val2+=round(float(a_val[2]),9)
    a_val3+=round(float(a_val[3]),9)
print(round((a_val1/len(lst)),9),round((a_val2/len(lst)),9), round((a_val3/len(lst)),9))

# with open('file_2.txt', 'r') as f:
#     strings = [s.rstrip() for s in f.readlines()]
#     print(strings)
# otsenki = [s.split(';')[1:] for s in strings]
# print(otsenki)
# for x in otsenki:
# # print(sum(map(int, x)) / len(x))
# sr_mat = sum([int(x[0]) for x in otsenki]) / len(otsenki)
# sr_fiz = sum([int(x[1]) for x in otsenki]) / len(otsenki)
# sr_rus = sum([int(x[2]) for x in otsenki]) / len(otsenki)
# print(sr_mat, sr_fiz, sr_rus)
