from tkinter import *
from tkinter import messagebox
import random


class Application(Frame):
    """"一个经典的GUI程序"""
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()

    def createWidget(self):
       """创建组建"""
       self.canvas =Canvas(self,width=300,height=200,gb="green")
       self.canvas.pack()
       line = self.canvas.create_line(10,10,30,20,40,50)
       rect =self.canvas.create_rectangle(50,50,100,100)
       oval = self.canvas.create_oval(50,50,100,100)
       global photo
       photo =PhotoImage("images/test.gif")
       self.canvas.create_image(150,170,image=photo)
       Button(self,text="画10个矩形",command=self.draw50Recg).pack(side="left")

    def draw50Recg(self):
            for i in range(0,10):
                x1=random.randrange(int(self.canvas["width"])/2)
                y1=random.randrange(int(self.canvas["height"])/2)
                x2=x1+random.randrange(int(self.canvas["width"])/2)
                y2 = y2+random.randrange(int(self.canvas["height"]) / 2)
                self.canvas.create_rectangle(x1,y1,x2,y2)


if __name__ == '__main__':
    root = Tk()
    root.geometry("600x400+200+300")
    root.title("GUI")
    app = Application(master=root)
    root.mainloop()