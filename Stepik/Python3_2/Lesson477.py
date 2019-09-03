def rangetest(*argchecks):
    def onDecoranor(func):
        if not __debug__:
            return func
        else:
            def onCall(*args):
                return func(*args)
        return onCall
    return onDecoranor

class Person:
    @rangetest(0.0,1.0)
    def giveRise(self, percent):
        self.pay = int(self.pay*(1+percent))

x = Person()
x.giveRise(0, 0.8)