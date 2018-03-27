from tkinter import *

class ComputeTable:
    to_compute = ""
    num_rows = 0
    variables = []
    sub_expressions = []

    def __init__(self, expression):
        self.to_compute = expression
        root = Tk()
        canvas = Canvas(root)
        canvas.pack(fill=BOTH, expand=1)
        self.gen_vars()
        self.tryExec(canvas)
        root.mainloop()

    def tranformImplication(self, string):
        # *** sub-string until implication ***
            result = ""
            result = "not("+string[0:len(string)-2]+")"+"or"
            return result

    def tryExec(self,canvas):
        to_exec = ""
        numVar = len(self.variables)
        truth_table = []
        result=[]

        if numVar == 2:
            truth_table = [[True,True,False,False],[False, True, False, True]]
        elif numVar == 3:
            truth_table =[
                          (True, True, True, True, False, False, False, False),
                          (True, True, False, False, True, True, False, False),
                          (True, False, True, False, True, False, True, False)
                        ]
        else:
            truth_table = [(True, False)]
        displacement = 30
        for i in range(len(self.to_compute)):
            if self.to_compute[i] == "/" and self.to_compute[i+1] == "\\":
                to_exec+=" and "
            elif self.to_compute[i] == "\\" and self.to_compute[i + 1] == "/":
                to_exec+=" or "
            elif self.to_compute[i] == "X":
                to_exec += " ^ "
            elif self.to_compute[i] == "<" and self.to_compute[i+1] == "-" and self.to_compute[i+2] == ">":
                to_exec += " == "
            elif self.to_compute[i] in self.variables:
                to_exec += " "+self.to_compute[i]+" "
            elif self.to_compute[i] == "~":
                to_exec+= " not "
            elif self.to_compute[i] == "(":
                to_exec += " ( "
            elif self.to_compute[i] == ")":
                to_exec += " ) "

        if numVar == 2:
            displacement = 70
            desplasamientos = [100, 170]
            verticalStart = 50
            for i in range(len(truth_table[0])):
                new = str()
                if self.variables[0] == "v":
                    new = to_exec.replace("v", "bool("+str(truth_table[0][i])+")")
                elif self.variables[0] == "p":
                    new = to_exec.replace("p", "bool("+str(truth_table[0][i])+")")
                elif self.variables[0] == "q":
                    new = to_exec.replace("q", "bool("+str(truth_table[0][i])+")")
                canvas.create_text(desplasamientos[0],verticalStart, text= str(truth_table[0][i]))
                if self.variables[1] == "v":
                    new = new.replace("v", "bool("+str(truth_table[1][i])+")")
                elif self.variables[1] == "p":
                    new = new.replace("p", "bool("+str(truth_table[1][i])+")")
                elif self.variables[1] == "q":
                    new = new.replace("q", "bool("+str(truth_table[1][i])+")")
                canvas.create_text(desplasamientos[1], verticalStart, text=str(truth_table[1][i]))
                verticalStart+=50
                print(new)

                if len(self.variables) == 2:
                    start_x = 100
                    # *** draw variables *** #
                    for i in self.variables:
                        canvas.create_text(start_x, 20, text=i)
                        start_x += 70
                canvas.create_text(300, 20, text=to_exec)
                exec("canvas.create_text("+str(300)+","+str(displacement-20)+", text=str("+new.strip(" ")+"))")
                displacement += 50

        elif numVar == 3:
            desplasamientos = [50,120,190]
            startY = 30
            for i in range(len(truth_table[0])):
                new = str()
                if self.variables[0] == "v":
                    new = to_exec.replace("v", "bool(" + str(truth_table[0][i]) + ")")
                elif self.variables[0] == "p":
                    new = to_exec.replace("p", "bool(" + str(truth_table[0][i]) + ")")
                elif self.variables[0] == "q":
                    new = to_exec.replace("q", "bool(" + str(truth_table[0][i]) + ")")
                canvas.create_text(desplasamientos[0], startY, text=str(truth_table[0][i]))
                if self.variables[1] == "v":
                    new = new.replace("v", "bool(" + str(truth_table[1][i]) + ")")
                elif self.variables[1] == "p":
                    new = new.replace("p", "bool(" + str(truth_table[1][i]) + ")")
                elif self.variables[1] == "q":
                    new = new.replace("q", "bool(" + str(truth_table[1][i]) + ")")
                canvas.create_text(desplasamientos[1], startY, text=str(truth_table[1][i]))
                if self.variables[2] == "v":
                    new = new.replace("v", "bool(" + str(truth_table[2][i]) + ")")
                elif self.variables[2] == "p":
                    new = new.replace("p", "bool(" + str(truth_table[2][i]) + ")")
                elif self.variables[2] == "q":
                    new = new.replace("q", "bool(" + str(truth_table[2][i]) + ")")
                canvas.create_text(desplasamientos[2], startY, text=str(truth_table[2][i]))
                startY+=30
                print(new)
                if len(self.variables) == 3:
                    start_x = 50
                    # *** draw variables *** #
                    for i in self.variables:
                        canvas.create_text(start_x, 10, text=i)
                        start_x += 70
                canvas.create_text(300, 10, text = to_exec)
                exec("canvas.create_text(" + str(300) + "," + str(displacement) + ", text=str(" + new.strip(" ") + "))")
                displacement += 30


    def generate_table_header(self):
        stack = []
        simple_stack = []
        last_expression = ""
        if "(" not in self.to_compute and ")" not in self.to_compute:
            for i in range(len(self.to_compute)):
                if self.to_compute == "~" and self.to_compute[i+1] in self.variables:
                    simple_stack.append("~"+self.to_compute[i+1])
                if self.to_compute[i] == "/" and self.to_compute[i+1] == "\\":
                    try:
                        if self.to_compute[i-2] == "~" and self.to_compute[i-1] in self.variables:
                            if self.to_compute[i+1] == "~" and self.to_compute[i+2] in self.variables:
                                simple_stack.append(self.to_compute[i-2:i+3])
                                
                    except:
                        pass




    def gen_vars(self):
        varCount = 0
        self.variables = []
        if "p" in self.to_compute and "p" not in self.variables:
            self.variables.append("p")
        if "q" in self.to_compute and "q" not in self.variables:
            varCount += 1
            self.variables.append("q")
        if "v" in self.to_compute and "v" not in self.variables:
            varCount += 1
            self.variables.append("v")
        self.num_rows = 2**varCount
        print(self. variables)
        print(self.num_rows)



