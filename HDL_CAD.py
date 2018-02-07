

class inOut():
    input = False
    size = 1
    name = ""

    def __init__(self,input,size,name):
        self.input = input
        self.size = size
        self.name = name

    def generate(self):

        if self.size ==1 and self.input:
            return ("input " + self.name)
        elif self.size > 1 and (self.input == True):
            return ("input ["+str(self.size-1) + ":0] " + self.name )
        elif self.size == 1 and (self.input == False):
            return ("output " + self.name )
        elif self.size > 0 and (self.input == False):
            return ("output ["+str(self.size-1) + ":0] " + self.name )



class Module():

    module = ""
    name = ""
    inputs = []
    outputs = []
    parameter = None
    modules = []
    assignments = []

    def __init__(self, name, parameter):
        self.name = name
        self.parameter = parameter

    def addInput(self, identifier, bus):

        input = inOut(True,bus,identifier)
        self.inputs.append(input)

    def addOutput(self, identifier, bus):

        output = inOut(False, bus, identifier)
        self.outputs.append(output)

    def addAssign(self,LHS1,LHS2,operator,RHS):
        self.assignments.append(RHS + "=" + LHS1 + operator + LHS2)

    def generateTitle(self):
        Title ="module " + self.name + " #" + str(self.parameter) +" ("
        for key in self.inputs:
            Title += key.generate() + ", "
        for key in self.outputs:
            Title += key.generate()
            if key != self.outputs[-1]:
                Title += ","
        Title += ");"
        print(Title)

    # def generateInputs(self):
    #
    #     InputSet = ""
    #     for key in self.inputs:
    #         InputSet += key.generate() +"\n"
    #     print(InputSet)
    #
    # def generateOutputs(self):
    #
    #         OutputSet = ""
    #         for key in self.outputs:
    #             OutputSet += key.generate() + "\n"
    #         print(OutputSet)

    def generateAssigns(self):
        AssignSet = ""
        for key in self.assignments:
            AssignSet +="assign" +  key + "\n"
        print(AssignSet)



def main():
    And = Module("and", 1)
    And.addInput("a", 5)
    And.addInput("b", 3)
    And.addOutput("c",1)
    And.addAssign("a", "b", "&","c")
    And.generateTitle()
    # And.generateInputs()
    # And.generateOutputs()
    #And.generateAssigns()
    print("end module")

if __name__ == '__main__':
    main()






