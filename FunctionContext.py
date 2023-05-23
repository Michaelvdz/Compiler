class FCStack:

    functions = []

    def __init__(self):
        self.functions = []

    def pop(self):
        return self.functions.pop()

    def push(self, function):
        self.functions.append(function)
        #print("Added table")
        #print(len(self.tables))

    def peek(self):
        function = self.functions.pop()
        #print("Peeking at:")
        #print(table.name)
        self.functions.append(function)
        return function

    def getCurrentOffset(self):
        function = self.functions.pop()
        self.functions.append(function)
        return function.offset

    def getRestoreOffset(self):
        function = self.functions.pop()
        self.functions.append(function)
        return function.roffset

    def getFreeTempReg(self):
        function = self.functions.pop()
        self.functions.append(function)
        return function.getFreeTempReg()

    def getFreeFTempReg(self):
        function = self.functions.pop()
        self.functions.append(function)
        return function.getFreeFTempReg()

    def addTempReg(self, reg):
        function = self.functions.pop()
        self.functions.append(function)
        return function.addTempReg(reg)

    def removeTempReg(self, reg):
        function = self.functions.pop()
        self.functions.append(function)
        return function.removeTempReg(reg)

class FunctionContext:

    offset = 0
    roffset = 0

    regs = dict()

    def __init__(self):
        offset = 0
        roffset = 0

    def getFreeTempReg(self):
        for i in range(0, 7):
            if not self.regs.get("$t"+str(i)):
                return i

    def addTempReg(self, reg):
        self.regs[reg] = "used"

    def removeTempReg(self, reg):
        self.regs.pop(reg)

    def getFreeFTempReg(self):
        print("Finding free F")
        for i in range(0, 31):
            if not self.regs.get("$f"+str(i)):
                return i

