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
       self.lable01=Label(self,text="用户名")
       self.lable01.pack()

       v1=StringVar()
       self.entry01 =Entry(self,textvariable=v1)
       self.entry01.pack()
       v1.set("admin")

       self.lable02 = Label(self, text="密码")
       self.lable02.pack()

       v2 = StringVar()
       self.entry02 = Entry(self, textvariable=v2,show="*")
       self.entry02.pack()
       v1.set("admin")

       self.btn01 = Button(self, text="登陆", width="16", command=self.login)
       self.btn01.pack()

    def login(self):
        print("用户名:"+self.entry01.get())
        print("密码:"+self.entry02.get())
        messagebox.showinfo("学习系统","登录成功，欢迎学习！")
if __name__ == '__main__':
    root = Tk()
    root.geometry("400x400+200+300")
    root.title("GUI")
    app = Application(master=root)
    root.mainloop()
