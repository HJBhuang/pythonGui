from tkinter import *#line:1
from tkinter import messagebox #line:2
class Application (Frame ):#line:4
    ""#line:5
    def __init__ (OO0OOO0OO0O0OO0O0 ,master =None ):#line:6
        super ().__init__ (master )#line:7
        OO0OOO0OO0O0OO0O0 .master =master #line:8
        OO0OOO0OO0O0OO0O0 .pack ()#line:9
        OO0OOO0OO0O0OO0O0 .createWidget ()#line:10
    def createWidget (O00OOOOOOO0O00O00 ):#line:12
       ""#line:13
       O00OOOOOOO0O00O00 .label01 =Label (O00OOOOOOO0O00O00 ,text ="用户名")#line:15
       O00OOOOOOO0O00O00 .label01 .grid (row =0 ,column =0 )#line:16
       O00OOOOOOO0O00O00 .entry01 =Entry (O00OOOOOOO0O00O00 )#line:17
       O00OOOOOOO0O00O00 .entry01 .grid (row =0 ,column =1 )#line:18
       Label (O00OOOOOOO0O00O00 ,text ="用户手机号").grid (row =0 ,column =2 )#line:20
       Entry (O00OOOOOOO0O00O00 ).grid (row =0 ,column =3 )#line:21
       O00OOOOOOO0O00O00 .label02 =Label (O00OOOOOOO0O00O00 ,text ="密码")#line:23
       O00OOOOOOO0O00O00 .label02 .grid (row =1 ,column =0 )#line:24
       O00OOOOOOO0O00O00 .entry02 =Entry (O00OOOOOOO0O00O00 )#line:25
       O00OOOOOOO0O00O00 .entry02 .grid (row =1 ,column =1 )#line:26
       Button (O00OOOOOOO0O00O00 ,text ="登录").grid (row =2 ,column =1 ,sticky =EW )#line:28
       Button (O00OOOOOOO0O00O00 ,text ="取消").grid (row =2 ,column =3 ,sticky =EW )#line:29
if __name__ =='__main__':#line:31
    root =Tk ()#line:32
    root .geometry ("600x400+200+300")#line:33
    root .title ("GUI")#line:34
    app =Application (master =root )#line:35
    root .mainloop ()#line:36
