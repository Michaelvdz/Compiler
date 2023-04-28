class Node:
    def __init__(self, constant, type, value, attr="", node=""):
        self.constant = constant
        self.type = type
        self.attr = attr
        self.register = None
        self.astnode = node

    def __str__(self):
        return f'{self.type} and attr: {self.attr} and register: {self.register}'

class Function(Node):
    def __init__(self, totalParams, constant, type, value, attr="", node="", params=[]):
        self.constant = constant
        self.type = type
        self.attr = attr
        self.register = None
        self.astnode = node
        self.params = []
        self.totalParams = totalParams

    def __str__(self):
        return f'{self.type} and attr: {self.attr} and register: {self.register} and params:'


class Array(Node):
    def __init__(self, constant, type, size, attr="", node=""):
        print("Size: " + size)
        self.constant = constant
        self.type = type
        self.attr = attr
        self.register = None
        self.astnode = node
        self.size = size

    def __str__(self):
        return f'{self.type} and attr: {self.attr} and register: {self.register} and size {self.size}'



class SymbolTables:

    tables = []
    def __int__(self):
        self.tables = []

    def empty(self):
        for child in self.tables:
            self.tables.remove(child)

    def pop(self):
        return self.tables.pop()

    def push(self, table):
        self.tables.append(table)
        print("Added table")
        print(len(self.tables))

    def peek(self):
        table = self.tables.pop()
        #print("Peeking at:")
        #print(table.name)
        self.tables.append(table)
        return table
    
    def search(self, name):
        for i in self.tables:
            listOfKeys = i.vars.keys()
            if name in listOfKeys:
                return True, i.vars[name].totalParams, i.vars[name].type
        return False, 0, 0

class SymbolTable:

    name = ""
    parent = 0
    children = []
    vars = dict()

    def __init__(self):
        self.vars = dict()
        self.children = list()
        self.children.clear()
        self.parent = 0
        self.name = ""

    def __str__(self):
        string = []
        string.append("Table with name: " + self.name + "\n")
        for key, value in self.vars.items():
            string.append(str(key) + ": " + str(value) + "\n")

        string.append("#Children: " + str(len(self.children)))
        return "".join(string)

    def print(self):
        print("Table with name: " + self.name + "\n")
        '''
        for key, value in self.vars.items():
            #print(str(key) + ": " + str(value.type) + "attr: " + str(value.attr) + "register: " + str(value.register) +  "\n")
            print("Children")
        '''

        print("Printring vars:")
        for key, value in self.vars.items():
            print(str(key) + ": " + str(value))

        print("With children: ")
        for child in self.children:
            child.print()
        print("End of table: " + self.name)

    def insert(self, name, constant, type, attribute=""):
        self.vars[name] = Node(constant, type, "", attribute)

    def insertFunction(self, name, totalParams, constant, type, attribute="", node="", params=[]):
        self.vars[name] = Function(totalParams, constant, type, "", attribute, node, params)

    def insertArray(self, name, constant, type, attribute, size):
        print("Inserting array with size:" + str(size))
        self.vars[name] = Array(constant, type, size, "", attribute)

    def insertRegister(self, name, register):
        #print("Zoeken naar var: " + name + "in scope: " + self.name)
        if self.vars.get(name):
            self.vars[name].register = register
        else:
            if self.parent:
                self.parent.insertRegister(name, register)



    def lookup(self, name):
        var = self.vars.get(name)
        if var:
            return var
        else:
            if self.parent:
                return self.parent.lookup(name)
        #print("Nothing found")
        return 0

    def lookupInThisTable(self, name):
        var = self.vars.get(name)
        if var:
            return var
        else:
            return 0

    def lookupByRegister(self, register):
        for key, value in self.vars.items():
            if self.vars[key].register == register:
                return self.vars[key]
        if self.parent:
            return self.parent.lookupByRegister(register)
        return 0

    def replaceRegisters(self, old, new):
        for key, value in self.vars.items():
            if self.vars[key].register == old:
                self.vars[key].register = new
        return 0
