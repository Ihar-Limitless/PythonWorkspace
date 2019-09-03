class A:
    pass

class B(A):
    pass

class C:
    pass

class D:
    pass

class E(B, C, D):
    pass
e = E()
print(E.mro())