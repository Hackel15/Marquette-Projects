from tkinter import *

class ConvertGUI():
    def __init__(self):
        self.top = Tk()
        self.top.title("Conversion")
        self.top.geometry("300x100")
        self.defineWidgets()
        self.top.mainloop()

    def defineWidgets(self):

        self.label1 = Label(self.top,text="kgs")
        self.label1.grid(row=1,column=3)
        
        self.label2 = Label(self.top,text="is equal to")
        self.label2.grid(row=2,column=1)

        self.label3 = Label(self.top)
        self.label3.grid(row=2,column=2)
        
        self.label4 = Label(self.top,text="lbs")
        self.label4.grid(row=2,column=3)

        self.weight_kg = StringVar()
        self.kg_entry = Entry(self.top,textvariable = self.weight_kg)
        self.kg_entry.grid(row=1,column=2)

        self.calbutton = Button(self.top,text="Calculate",command = self.convert)
        self.calbutton.grid(row=3,column=3)

    def convert(self):
        try:
            weight_lb = 2.20462*(float(self.weight_kg.get()))
            self.label3.config(text=weight_lb)
        except ValueError:
            pass

call = ConvertGUI()
