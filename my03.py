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
       self.label01=Label(self,text='百战程序员',width=10,height=2,bg='black',fg='white')
       self.label01.pack()

       self.label02=Label(self,text='百战程序员',width=10,height=2,bg='blue',fg='black',font=("黑体",30))
       self.label02.pack()

       global  photo #必须设置为全局变量
       photo = PhotoImage(file="images/test.gif")
       self.lable03 =Label(self,image=photo)
       self.lable03.pack()

        #多文本换行
       self.label04 = Label(self,text="北京尚学堂\n百战程序员\n老高好帅，就是做饭不行",
                            borderwidth=1,relief="solid",justify="right")
       self.label04.pack()

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x400+200+300")
    root.title("GUI")
    app = Application(master=root)
    root.mainloop()
