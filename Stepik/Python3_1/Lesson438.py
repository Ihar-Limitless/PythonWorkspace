import operator
name = [('Vasiliy', 'Ivanovoch', 'Chapaev'), ('Anka', 'Pulemetchitsa'),('Prosto','Petka')]
# def name_length(name):
#     return len(" ".join(name))
#
# name.sort(key = name_length)
# print(name)

name.sort(key=lambda n: len(" ".join(n)))
print(name)

x = [1,2,3,4,5]
func = operator.itemgetter(2)
print(func(x))