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
       self.btn01=Button(self)
       self.btn01["text"] = "点我就送花"
       self.btn01.pack()
       self.btn01["command"] = self.songhua

        #创建退出按钮
       self.btnQuit = Button(self,text="退出",command= root.destroy)
       self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo("Message","送你一朵花")


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x100+200+300")
    root.title("一个经典的GUI程序")
    app = Application(master=root)
    root.mainloop()
