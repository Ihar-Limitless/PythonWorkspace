class Base:
    def __init__(self):
        print("- class Base init")
        self.val = 0

    def add_one(self):
        print("- class Base add_one")
        self.val += 1

    def add_many(self, x):
        print("- class Base add_many")
        for i in range(x):
            self.add_one()

class Derived(Base):
    def add_one(self):
        print("- class Derived add_one")
        self.val += 10

a = Derived()
a.add_one()
print("a =", a.val, "******")
b = Derived()
b.add_many(3)
print("b =", b.val, "******")
