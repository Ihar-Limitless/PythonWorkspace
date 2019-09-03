class A:
    def __init__(self, val=0):
        self.val = val

    def add(self, x):
        self.val += x

    def print_val(self):
        print(self.val)


a = A()
a.print_val()