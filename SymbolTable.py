class Node:
    def __init__(self, constant, type, value, attr=""):
        self.constant = constant
        self.type = type
        self.attr = attr
        self.register = None

    def __str__(self):
        return f'{self.type} and attr: {self.attr} and register: {self.register}'


class SymbolTable:
    def __init__(self):
        self.vars = dict()

    def __str__(self):
        string = []
        for key, value in self.vars.items():
            string.append(str(key) + ": " + str(value))
        return "\n".join(string)

    def insert(self, name, constant, type, attribute=""):
        self.vars[name] = Node(constant, type, "", attribute)

    def insertRegister(self, name, register):
        self.vars[name].register = register

    def lookup(self, name):
        var = self.vars.get(name)
        if var:
            return var
        else:
            return 0

    def lookupByRegister(self, register):
        print("Searching vor regs")
        for key, value in self.vars.items():
            if self.vars[key].register == register:
                return self.vars[key]
        return 0

    def replaceRegisters(self, old, new):
        for key, value in self.vars.items():
            if self.vars[key].register == old:
                self.vars[key].register = new
        return 0