class MaxAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        self.maxNumIdx = 0

    def setMaxIdxAndNum(self):
        self.maxNum = 0
        self.maxNumIdx = 0

        for i, n in enumerate(self.nums):
            if self.maxNum < n:
                self.maxNum = n
                self.maxNumIdx = i

        return self.maxNum

    def getMaxNum(self):
        return self.maxNum

    def getMaxNumIdx(self):
        return self.maxNumIdx;