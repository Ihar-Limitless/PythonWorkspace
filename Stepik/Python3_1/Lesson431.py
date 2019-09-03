def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

class multifilter:

    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):

        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for el in self.iterable:
            pos = 0
            neg = 0
            for func in self.funcs:
                if func(el):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield el

print(list(multifilter(a, mul2, mul3, mul5)))


# class multifilter:
#     judge_half = lambda fx: sum(fx) >= len(fx) / 2
#     judge_any = lambda fx: any(fx)
#     judge_all = lambda fx: all(fx)
#
#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.iterable = iterable
#         self.funcs = funcs
#         self.judge = judge
#
#     def __iter__(self):
#         return (x for x in self.iterable if self.judge([f(x) for f in self.funcs]))