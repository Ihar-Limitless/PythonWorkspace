import collections
#str = input().strip().lower().split()
dct = [count for count in input().strip().lower().split()]
# for key in str:
#     if key in dct:
#         dct[key] += 1
#     else:
#         dct[key] = 1
# for key in dct:
#     print("{} {}".format(key, dct[key]))

c = collections.Counter(dct)
for key, val in c.items():
    print(key,val)

