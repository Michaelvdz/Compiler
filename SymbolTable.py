class Node:
    def __init__(self, type, value):
        self.type = type
        self.value = value


class SymbolTable:
    def __init__(self):
        self.vars = dict()

    def insertTable(self, type, value):
        self.vars[value] = Node(type, value)
