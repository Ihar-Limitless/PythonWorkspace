class ThirdClass():
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return (self.data + other)
    def __str__(self):
        return '[ThirdClass: %s]' % self.data
    def display(self):
        print('current value is %s' % self.data)
    def mul(self, other):
        self.data *= other
a = ThirdClass("abc")
a.display()
b = a
a.mul(3)
print(a)
print(a.__dict__.keys())
def lalala(self):
    return self.data.upper()
ThirdClass.method = lalala
print(a.method())