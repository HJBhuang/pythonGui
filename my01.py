from tkinter import *
from tkinter import messagebox


# 黄佳宝
# 2020/1/5
#
root = Tk()
root.title("我是第一个GUI")
root.geometry("500x300+300+100")
btn01 = Button(root)
btn01["text"]="点我就送花"
btn01.pack()


def songhua(e):  # e事件对象
    messagebox.showinfo("Message","送你一朵花")
    print("送你一朵花")

btn01.bind("<Button-1>",songhua)
root.mainloop()
