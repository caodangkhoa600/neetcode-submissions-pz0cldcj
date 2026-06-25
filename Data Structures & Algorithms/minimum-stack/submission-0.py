class MinStack:
    __minValue = None
    data = []
    currentIndex = 0

    def __init__(self):
        self.__minValue = None
        self.data = []
        self.currentIndex = -1

    def push(self, value: int) -> None:
        if self.__minValue == None or self.__minValue > value:
            self.__minValue = value

        if self.currentIndex + 1 == len(self.data):
            self.currentIndex = self.currentIndex + 1
            self.data.append(value)
        else:
            self.currentIndex = self.currentIndex + 1
            self.data[self.currentIndex] = value

    def pop(self) -> None:
        result = self.data[self.currentIndex]
        self.data[self.currentIndex] = None
        self.currentIndex = self.currentIndex - 1
        crrA = self.data[0:self.currentIndex + 1]
        
        if len(crrA) == 0:
            self.__minValue = None
            return

        self.__minValue = min(self.data[0:self.currentIndex + 1])
        return result

    def top(self) -> int:
        return self.data[self.currentIndex]

    def getMin(self) -> int:
        return self.__minValue
