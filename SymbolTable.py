class Node:
    def __init__(self, constant, type, value, attr=""):
        self.constant = constant
        self.type = type
        self.attr = attr

    def __str__(self):
        return f'{self.type} and attr: {self.attr}'


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

    def lookup(self, name):
        var = self.vars.get(name)
        if var:
            return var
        else:
            return 0
