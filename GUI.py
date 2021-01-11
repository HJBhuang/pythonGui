from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *


class Application(Frame):
    """"一个经典的GUI程序"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.createWidget()

    def createWidget(self):
        """创建组建"""

        Button(root, text="选择文件", command=self.test1,font=("华文行楷",15)).place(x=20, y=36, width=180, height=30)
        # 使用 place() 设置该 Label 的大小和位置

        Button(root, text="开始处理", command=self.test1,font=("华文行楷",15)).place(x=320, y=36, width=180, height=30)

        Label(root, text="结果输出",font=("华文行楷",15)).place(x=20, y=80)

        self.show = Text(root, width=80, height=15, bg='white')
        self.show.place(x=20, y=120)


    def test1(self):
        f = askopenfilenames(title="上传文件", initialdir="c:", filetypes=[("文本", ".txt")])
        print(f)
        self.show.delete(1.0,END)
        self.show.insert(1.0,f)


if __name__ == '__main__':
    root = Tk()
    root.geometry("600x400+500+100")
    root.title("GUI")
    app = Application(master=root)
    root.mainloop()
