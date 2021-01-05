from tkinter import *
import webbrowser


class Application(Frame):
    """"一个经典的GUI程序"""
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()

    def createWidget(self):
       """创建组建"""
       self.w1=Text(self,width=40,height=12,bg="gray")
       self.w1.pack()
       self.w1.insert(1.0,"0123456789\nabcdefg")
       self.w1.insert(2.3,"锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦\n")
       Button(self,text="重复插入文本",command=self.insertText).pack(side="left")
       Button(self,text="返回文本",command=self.returnText).pack(side="left")
       Button(self,text="添加图片",command=self.addImage).pack(side="left")
       Button(self,text="添加组件",command=self.addWidget).pack(side="left")
       Button(self,text="通过tag精准控制文本",command=self.testTag).pack(side="left")

    def insertText(self):
        self.w1.insert(INSERT,'Gaoqi')
        self.w1.insert(END,'[sxt]')
        self.w1.insert(1.8, "gaoqi")
    def returnText(self):
        print(self.w1.get(1.2,1.6))

        print("所有文本内容:\n"+self.w1.get(1.0,END))


    def addImage(self):
        self.photo=PhotoImage(file="images/test.gif")
        self.w1.image_create(END,image=self.photo)

    def addWidget(self):
        b1=Button(self.w1,text="尚学堂")
        self.w1.window_create(INSERT,window=b1)
        pass
    def testTag(self):
        self.w1.delete(1.0,END)
        self.w1.insert(INSERT,"GOODGOODGOODGOODGOODGOOD\nGOODGOODGOODGOODGOOD\nGOODGOODGOODGOOD\nGOODGOODGOODGOODGOOD\nGOODGOODGOODGOOD\nGOODGOODGOODGOODGOOD\nGOODGOODGOODGOOD\nGOODGOODGOODGOODGOOD\nGOODGOODGOODGOOD")
        self.w1.tag_add("hjb",1.0,1.9)
        self.w1.tag_config("good",background='yellow',foreground="red")
        self.w1.tag_add("baidu",4.0,4.2)
        self.w1.tag_config("baidu",underline=True)
        self.w1.tag_bind("baidu","<Button-1>",self.webshow)
        pass
    def webshow(self,event):
        webbrowser.open("http://www.baidu.com")


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x400+200+300")
    root.title("GUI")
    app = Application(master=root)
    root.mainloop()
