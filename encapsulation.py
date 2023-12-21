class Unchanged:
    def __init__(self):
        self.__fixedVar = 88

    def getFixed(self):
        print(self.__fixedVar)

    def setFixed(self, fixed):
        self.__fixedVar = fixed

obj = Unchanged()
obj.getFixed()
obj.setFixed(44)
obj.getFixed()


