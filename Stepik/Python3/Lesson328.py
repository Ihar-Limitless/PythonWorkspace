import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, arg):
        print(LoggableList.mro())
        self.log(arg)
        super(LoggableList, self).append(arg)


a = LoggableList()
a.append(1)
print(a)
