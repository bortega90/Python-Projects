class Unchanged:
    def __init__(self):
        self.__fixedVar = 88 #private(__) instance attribute

    def getFixed(self):
        print(self.__fixedVar)

    def setFixed(self, fixed):
        self.__fixedVar = fixed

obj = Unchanged()
obj.getFixed()
obj.setFixed(44)
obj.getFixed()


class UnchangedProtected:
    def __init__(self):
        self._fixedVar = 5 #protected (_) instance attribute

obj = UnchangedProtected()
obj._fixedVar = 99
print(obj._fixedVar)
