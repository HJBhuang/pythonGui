from tkinter import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class Application(Frame):
    """一个经典的GUI写法"""

    def __init__(self, master=None):
        '''初始化方法'''
        super().__init__(master)  # 调用父类的初始化方法
        self.master = master
        self.pack(side=TOP, fill=BOTH, expand=1)  # 此处填充父窗体
        self.create_matplotlib()
        self.createWidget(self.figure)

    def createWidget(self, figure):
        """创建组件"""
        self.label = Label(self, text='这是一个Tkinter和Matplotlib相结合的小例子')
        self.label.pack()
        # 创建画布
        self.canvas = FigureCanvasTkAgg(figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        # 把matplotlib绘制图形的导航工具栏显示到tkinter窗口上
        # toolbar = NavigationToolbar2Tk(self.canvas, self)
        # toolbar.update()
        # self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
        # self.button = Button(master=self, text="退出", command=quit)
        # # 按钮放在下边
        # self.button.pack(side=BOTTOM)

    def create_matplotlib(self):
        """创建绘图对象"""
        # 设置中文显示字体
        mpl.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
        mpl.rcParams['axes.unicode_minus'] = False  # 负号显示
        # 创建绘图对象f figsize的单位是英寸 像素 = 英寸*分辨率
        self.figure = plt.figure(num=2, figsize=(2, 3), dpi=80, facecolor="gold", edgecolor='green', frameon=True)
        # 创建一副子图
        fig1 = plt.subplot(1, 1, 1)  # 三个参数，依次是：行，列，当前索引
        # 创建数据源：x轴是等间距的一组数
        x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
        y1 = np.sin(x)
        y2 = np.cos(x)

        line1 = fig1.plot(x, y1, color='red', linewidth=2, label='y=sin(x)', linestyle='--')  # 画第一条线
        line2 = fig1.plot(x, y2, color='green', label='y=cos(x)')
        plt.setp(line2, linewidth=1, linestyle='-', alpha=0.7)  # 华第二条线 color='',

        fig1.set_title("数学曲线图", loc='center', pad=20, fontsize='xx-large', color='red')  # 设置标题
        # line1.set_label("正弦曲线")  # 确定图例
        # 定义legend 重新定义了一次label
        fig1.legend(['正弦', '余弦'], loc='lower right', facecolor='orange', frameon=True, shadow=True, framealpha=0.7)
        # ,fontsize='xx-large'
        fig1.set_xlabel('(x)横坐标')  # 确定坐标轴标题
        fig1.set_ylabel("(y)纵坐标")
        fig1.set_yticks([-1, -1 / 2, 0, 1 / 2, 1])  # 设置坐标轴刻度
        fig1.grid(which='major', axis='x', color='gray', linestyle='-', linewidth=0.5, alpha=0.2)  # 设置网格

    def destroy(self):
        """重写destroy方法"""
        super().destroy()
        quit()

    def quit():
        """点击退出按钮时调用这个函数"""
        root.quit()  # 结束主循环
        root.destroy()  # 销毁窗口


if __name__ == '__main__':
    root = Tk()
    root.title('数学曲线窗口')
    root.geometry('1000x700+200+10')
    app = Application(master=root)

    root.mainloop()