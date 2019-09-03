class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError

# _____________________________________
# class PositiveList(list):
#     def append(self, arg):
#         if arg > 0:
#             list.append(self, arg)
#         else:
#             raise NonPositiveError
# _____________________________________

lst = PositiveList()
for i in range(-10,10):
    lst.append(i)
print(lst)



