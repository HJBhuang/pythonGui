from tkinter import *
from tkinter import messagebox

class Application(Frame):
    """"一个经典的GUI程序"""
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()

    def createWidget(self):
       """创建组建"""

       self.label01=Label(self,text="用户名")
       self.label01.grid(row=0,column=0)
       self.entry01=Entry(self)
       self.entry01.grid(row=0,column=1)

       Label(self,text="用户手机号").grid(row=0,column=2)
       Entry(self).grid(row=0,column=3)

       self.label02 = Label(self, text="密码")
       self.label02.grid(row=1, column=0)
       self.entry02 = Entry(self)
       self.entry02.grid(row=1, column=1)

       Button(self,text="登录").grid(row=2,column=1,sticky=EW)
       Button(self,text="取消").grid(row=2,column=3,sticky=EW)

if __name__ == '__main__':
    root = Tk()
    root.geometry("600x400+200+300")
    root.title("GUI")
    app = Application(master=root)
    root.mainloop()
