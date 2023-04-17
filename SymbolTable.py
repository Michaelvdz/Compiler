class Node:
    def __init__(self, constant, type, value, attr=""):
        self.constant = constant
        self.type = type
        self.attr = attr
        self.register = None

    def __str__(self):
        return f'{self.type} and attr: {self.attr} and register: {self.register}'

class SymbolTables:

    tables = []
    def __int__(self):
        self.tables = []

    def pop(self):
        return self.tables.pop()

    def push(self, table):
        self.tables.append(table)

    def peek(self):
        table = self.tables.pop()
        print("Peeking at:")
        print(table.name)
        self.tables.append(table)
        return table

class SymbolTable:

    name = ""
    parent = 0
    children = []
    vars = dict()

    def __init__(self):
        self.vars = dict()
        self.children = []
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


        '''
        for child in self.children:
            child.print()
        '''

    def insert(self, name, constant, type, attribute=""):
        self.vars[name] = Node(constant, type, "", attribute)

    def insertRegister(self, name, register):
        print("Zoeken naar var: " + name + "in scope: " + self.name)
        if self.vars.get(name):
            print("Hij vindt de var")
            self.vars[name].register = register
        else:
            print("Hij vindt de var niet")
            if self.parent:
                print("Zoek bij parent")
                self.parent.insertRegister(name, register)



    def lookup(self, name):
        var = self.vars.get(name)
        if var:
            print("Var found, return it")
            return var
        else:
            print("Var not found, look at parent")
            print(self.parent)
            if self.parent:
                print("Looking at parent")
                return self.parent.lookup(name)
        print("Nothing found")
        return 0

    def lookupByRegister(self, register):
        print("Searching vor regs")
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