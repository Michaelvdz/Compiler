class Node:
    def __init__(self, constant, type, value, attr="", node=""):
        self.constant = constant
        self.type = type
        self.attr = attr
        self.register = None
        self.astnode = node
        self.inUse = False
        self.declared = False
        self.defined = False

    def __str__(self):
        return f'{self.type} and attr: {self.attr} and register: {self.register}'

    def print(self, tab, key):
        print(tab + "* " + key + " (Variable) with type: " + self.type)
        if self.attr:
            print(tab + "   " + self.attr)


class Function(Node):
    def __init__(self, totalParams, constant, type, value, attr="", node="", params=[]):
        self.constant = constant
        self.type = type
        self.attr = attr
        self.register = None
        self.astnode = node
        self.params = []
        self.totalParams = totalParams
        self.declared = False
        self.defined = False

    def __str__(self):
        return f'function with returntype {self.type} and attr: {self.attr} and register: {self.register} and params:'

    def print(self, tab, key):
        print(tab + "* " + key + " (Function) with (return)type: " + self.type)
        if self.params:
            print(tab+"   "+"with parameters:")
            for param in self.params:
                print(tab+"   "+param)
        else:
            print(tab+"   "+"with no parameters")


class Array(Node):
    def __init__(self, constant, type, size, attr="", node=""):
        #print("Size: " + size)
        self.constant = constant
        self.type = type
        self.attr = attr
        self.register = None
        self.astnode = node
        self.size = size
        self.inUse = False
        self.declared = False
        self.defined = False

    def __str__(self):
        return f'= {self.type} and attr: {self.attr} and register: {self.register} and size {self.size}'



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
        #print("Added table")
        #print(len(self.tables))

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
    analysisDone = False

    def __init__(self):
        self.vars = dict()
        self.children = list()
        self.children.clear()
        self.parent = 0
        self.name = ""
        self.analysisDone = False

    def __str__(self):
        string = []
        string.append("Table with name: " + self.name + "\n")
        for key, value in self.vars.items():
            string.append(str(key) + ": " + str(value) + "\n")

        string.append("#Children: " + str(len(self.children)))
        return "".join(string)

    def print(self, depth=0):
        tab = ""
        i = 0
        while i != depth:
            tab += "\t"
            i += 1
        tab2 = ""
        i = 0
        while i != depth+1:
            tab2 += "\t"
            i += 1

        print(tab+"Table with name: " + self.name)
        print(tab2+"Containing symbols:")
        for key, value in self.vars.items():
            #print(tab2 + str(key) + ": " + str(value))
            value.print(tab2, key)

        print(tab2+"With childtabels: ")
        newdepth = depth + 1
        for child in self.children:
            child.print(newdepth)
        if not self.children:
            print(tab2+"None")
        print(tab+"End of table: " + self.name)

    def insert(self, name, constant, type, attribute=""):
        self.vars[name] = Node(constant, type, "", attribute)

    def insertFunction(self, totalParams, name, constant, type, attribute="", node="", params=[]):
        self.vars[name] = Function(totalParams, constant, type, "", attribute, node, params)
        return self.vars[name]

    def insertArray(self, name, constant, type, attribute, size):
        #print("Inserting array with size:" + str(size))
        self.vars[name] = Array(constant, type, size, "", attribute)

    def insertRegister(self, name, register):
        #print("Zoeken naar var: " + name + "in scope: " + self.name)
        if self.vars.get(name):
            self.vars[name].register = register
        else:
            if self.parent:
                self.parent.insertRegister(name, register)


    def lookupActive(self, name):
        var = self.vars.get(name)
        if var:
            if var.register is not None:
                return var
        else:
            if self.parent:
                return self.parent.lookupActibe(name)
        #print("Nothing found")
        return 0

    def lookupUnallocated(self, name):
        var = self.vars.get(name)
        if var:
            return var
        else:
            if self.parent:
                return self.parent.lookupUnallocated(name)
        #print("Nothing found")
        return 0

    def lookupAnalysis(self, name):
        var = self.vars.get(name)
        if var:
            return var
        else:
            if self.parent:
                return self.parent.lookupAnalysis(name)
        #print("Nothing found")
        return 0

    def lookup(self, name):
        var = self.vars.get(name)
        if var:
            if var.register is not None or isinstance(var, Function):
                return var
            else:
                if self.parent:
                    return self.parent.lookup(name)
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

    def nextTable(self):
        for child in self.children:
            if not child.analysisDone:
                return child
        return self

    def loopInScopes(self):
        print(self.name)
        if "While" in self.name:
            return True
        else:
            if self.parent:
                return self.parent.loopInScopes()
            else:
                return False

    def functionInScopes(self):
        if "Global" in self.name:
            return False
        else:
            return True

    def getNumberOfVariables(self):
        size = 0
        size += len(self.vars.items())
        if self.children:
            for child in self.children:
                size += child.getNumberOfVariables()
            return size
        else:
            return size


