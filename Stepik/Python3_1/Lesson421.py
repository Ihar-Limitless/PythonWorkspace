from random import random
class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.k:
            self.i+=1
            return random()
        else:
            raise StopIteration

def random_generator(k):
    for i in range(k):
        yield random()

g = random_generator(5)
for i in g:
    print(i)