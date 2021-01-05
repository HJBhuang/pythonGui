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
       self.codeHobby = IntVar()
       self.videHobby = IntVar()
       self.c1=Checkbutton(self,text="敲代码",variable=self.codeHobby,onvalue=1,offvalue=0)
       self.c2=Checkbutton(self,text="看视频",variable=self.videHobby,onvalue=1,offvalue=0)
       self.c1.pack(side="left")
       self.c2.pack(side="left")
       Button(self,text="确定",command=self.confirm).pack(side="left")
    def confirm(self):
           if self.codeHobby.get() == 1:
               messagebox.showinfo("测试","敲代码")
           if self.videHobby.get() == 1:
               messagebox.showinfo("测试", "看视频")

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x400+200+300")
    root.title("GUI")
    app = Application(master=root)
    root.mainloop()
