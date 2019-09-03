from functools import reduce
# def myfunc(function, sequence):
#     tmp = sequence[0]
#     for i in sequence[1:]:
#         tmp = function(tmp, i)
#     return tmp
#
#
# print(myfunc(lambda x, y: x * y, [1, 2, 3, 4, 5]))

print(reduce(lambda x, y: x * y, [1,2,3,4,5]))
print(list(filter(lambda  x: x > 0, [0, -1, -2, 1, 2, 3, 4, 5])))
