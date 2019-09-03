class MixedNames:
    data = 'spam'
    def __init__(self, value):
        self.value = value
    def printer(self, newvalue):
        self.message = newvalue
        print(self.message)
ex1 = MixedNames(1)

print(ex1.data, ex1.value)
MixedNames.printer(ex1, 'new message')
print(ex1.message)

class NewMixed(MixedNames):
    def __init__(self , value1 = None):
        MixedNames.__init__(self, value1)
    def printer(self, nw1):
        self.message = nw1
        print("Переопределенный ", self.message)
ex2 = NewMixed()
MixedNames.printer(ex2, "10")
