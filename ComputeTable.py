from tkinter import *

class ComputeTable:
    to_compute = ""
    num_rows = 0
    variables = []
    sub_expressions = []

    def __init__(self, expression):
        self.to_compute = expression
        root = Tk()

        root.mainloop()


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




    def gen_num_columns(self):
        varCount = 0
        if "p" in self.to_compute:
            varCount += 1
            self.variables.append("p")
        if "q" in self.to_compute:
            varCount += 1
            self.variables.append("q")
        if "r" in self.to_compute:
            varCount += 1
            self.variables.append("r")
        self.num_rows = 2**varCount
        print(self. variables)
        print(self.num_rows)



