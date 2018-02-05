


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

    def addOutput(self, identifier, bus):
        self.outputs[identifier] = bus


    def addAssign(self,LHS1,LHS2,operator,RHS):
        self.assignments.append(RHS + "=" + LHS1 + operator + LHS2)

    def generateTitle(self):
        Title ="module " + self.name + " #" + str(self.parameter) +" ("
        for key in self.inputs:
            Title += key + ", "
        for key in self.outputs:
            Title += key + ", "
        Title += ");"
        print(Title)

    def generateInputs(self):

        InputSet = ""
        for key in self.inputs:
            InputSet += "input [" + str(self.inputs[key]-1) + ":0]" + key +"\n"
        print(InputSet)

    def generateOutputs(self):

            OutputSet = ""
            for key in self.outputs:
                OutputSet += "output [" + str(self.outputs[key] - 1) + ":0]" + key + "\n"
            print(OutputSet)

    def generateAssigns(self):
        AssignSet = ""
        for key in self.assignments:
            AssignSet +="assign" +  key + "\n"
        print(AssignSet)



def main():
    And = Module("and", 1)
    And.addInput("a", 1)
    And.addInput("b", 1)
    And.addOutput("c",1)
    And.addAssign("a", "b", "&","c")
    And.generateTitle()
    And.generateInputs()
    And.generateOutputs()
    And.generateAssigns()
    print("end module")

if __name__ == '__main__':
    main()






