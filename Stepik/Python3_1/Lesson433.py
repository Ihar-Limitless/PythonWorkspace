a = [-1, -2, -4, 1, 5, 7, 9, -8, 10]
def selfGenerator(val):
    for i in val:
        if i > 0:
            yield i
it = selfGenerator(a)

a = [i for i in range(5)]
print(a)