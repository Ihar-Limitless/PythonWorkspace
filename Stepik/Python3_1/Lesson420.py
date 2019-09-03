class DoubleIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        try:
            if self.i < len(self.lst):
                self.i += 2
                return self.lst[self.i - 2], self.lst[self.i - 1]
            else:
                StopIteration
        except IndexError:
            print('у вас нечетное количество!')
            raise IndexError

class MyList(list):
    def __iter__(self):
        return DoubleIterator(self)


for pair in MyList([1, 2, 3, 4, 5, 6, 7]):
    print(pair)
