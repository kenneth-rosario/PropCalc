from tkinter import *
from ComputeTable import ComputeTable

class Calculator:
    current_text = ""

    def set_text(self, text, label):
        self.current_text = text
        label.config(text=self.current_text)

    def compute(self,text, label):
        compute = ComputeTable(self.current_text)

    def __init__(self, root):

        # ******* Text Area ******* #

        topFrame = Frame(root)
        topFrame.pack(fill=X)
        CurrentText = Label(topFrame, text=self.current_text, bg="white", height=5)
        CurrentText.pack(fill=X)

        # ****** Button Area ****** #

        middleFrame = Frame(root, width=400, height=400)
        middleFrame.pack()

        # ****** Variables total of three ***** #

        p = Button(middleFrame, text="p", command=lambda: self.set_text(self.current_text+"p", CurrentText), width=10)
        q = Button(middleFrame, text="q", command=lambda: self.set_text(self.current_text+"q", CurrentText), width=10)
        r = Button(middleFrame, text="v", command=lambda: self.set_text(self.current_text+"v", CurrentText), width=10)
        p.grid(row=0, column=0)
        q.grid(row=0, column=1)
        r.grid(row=0, column=2)

        # ****** logic operators ****** #

        and_button = Button(middleFrame, text="/\\", command= lambda: self.set_text(self.current_text+"/\\",
                                                                                    CurrentText), width=10, height= 2)
        or_button = Button(middleFrame, text="\\/", command= lambda: self.set_text(self.current_text+"\\/",
                                                                                    CurrentText), width=10, height= 2 )
        exclusive_or = Button(middleFrame, text="XOr", command=lambda: self.set_text(self.current_text + "XOR",
                                                                                     CurrentText), width=10, height = 2)
        implication = Button(middleFrame, text="->", width=10, height = 2)
        biconditional = Button(middleFrame, text="<->", command= lambda: self.set_text(self.current_text+"<->",
                                                                                     CurrentText), width=10, height = 2)
        negation = Button(middleFrame, text="~", command= lambda: self.set_text(self.current_text+" ~",
                                                                                    CurrentText), width=10, height = 2)
        open_parenthsis = Button(middleFrame, text="(", command= lambda: self.set_text(self.current_text+"(",
                                                                                    CurrentText), width=10, height = 2)
        close_parenthesis = Button(middleFrame, text=")", command= lambda: self.set_text(self.current_text+")",
                                                                                    CurrentText), width=10, height = 2)
        delete = Button(middleFrame, text="C", command= lambda: self.set_text("", CurrentText), width=10, height = 2)
        compute = Button(middleFrame, text="gen_table", command= lambda:self.compute("", CurrentText), width=32)
        # position
        and_button.grid(row=1, column=0)
        or_button.grid(row=1, column=1)
        exclusive_or.grid(row=1, column=2)
        implication.grid(row=2, column=0)
        biconditional.grid(row=2, column = 1)
        negation.grid(row=2, column = 2)
        open_parenthsis.grid(row=3, column= 0)
        close_parenthesis.grid(row=3, column= 1)
        delete.grid(row=3, column=2)
        compute.grid(row=4, columnspan=3)
