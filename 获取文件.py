from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *



class Application(Frame):
    """"一个经典的GUI程序"""
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()

    def createWidget(self):
       """创建组建"""

       Button(self,text="选择文件",command=self.test1).pack()
       global show
       show =Label(self,width=600,height=10,bg='green')
       show.pack()

    def test1(self):
        f = askopenfilenames(title="上传文件",initialdir="c:",filetypes=[("文本",".*")])
        print(f)
        show["text"]=f

if __name__ == '__main__':
    root = Tk()
    root.geometry("600x400+200+300")
    root.title("GUI")
    app = Application(master=root)
    root.mainloop()
