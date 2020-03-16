import time
class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list,Loggable):
    def append(self, object):
        super(LoggableList, self).append(object)
        self.log(object)
a = LoggableList()
a.append(3)