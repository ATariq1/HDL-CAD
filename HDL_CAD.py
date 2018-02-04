


class Module():

    module = ""
    name = ""
    inputs = {}
    outputs = {}
    parameter = None
    modules = []
    assignments = []

    def __init__(self, name, parameter):
        self.name = name
        self.parameter = parameter

    def addInput(self, identifier, bus):
        self.inputs[identifier]= bus

    def addOuput(self, identifier, bus):
        self.inputs[identifier] = bus


    def addAssign(self,LHS,RHS,operator):
        self.assignments.append(LHS + operator + RHS)

    def generateTitle(self):
        Title = self.name + str(self.parameter) +"("
        for key in self.inputs:
            Title += key + ", "
        for key in self.outputs:
            Title += key + ", "
        Title += ");"
        print(Title)

    def generateInputs(self):

        InputSet = ""
        for key in self.inputs:
            InputSet += "input [" + str(self.inputs[key]-1) +":0]" + key +"\n"
        print(InputSet)


def main():
    And = Module("and", 1)
    And.addInput("a", 1)
    And.addInput("b", 1)
    And.addAssign("a", "b", "&")
    And.generateTitle()
    And.generateInputs()


if __name__ == '__main__':
    main()






