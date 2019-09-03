def one(arg1='BEST'):
    def two(arg2):
            def three(arg3):
                print(arg1 + ' ' + arg2 + ' ' + arg3)
            return three
    return two
one1 = one()
two = one1("the")
two("best!")
print(one.__annotations__)