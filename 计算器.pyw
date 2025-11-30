from tkinter import Tk
from ttkbootstrap import Button,Text
from ttkbootstrap.constants import *
window = Tk()
window.geometry('400x450')  # 设置窗口大小
window.title('计算器')  # 设置窗口标题
window.configure(background = 'white')#初始化窗口
list_ = ['','','']#初始化值列表

#输入数字
def charu(n):
    global text
    text.insert('end',n,"right")

#运算符
def operation(n):
    global text
    global small_text
    global list_
    try:
        list_[0] = int(text.get('1.0', 'end').strip())
    except:
        list_[0] = float(text.get('1.0', 'end').strip())
    list_[1] = n
    small_text.delete('1.0', 'end')
    small_text.insert('end',str(list_[0]),"right")
    text.delete('1.0','end')

#等号
def equal():
    global text
    global small_text
    global list_
    if list_[1] == '':
        pass
    else:
        try :
            list_[2] = int(text.get('1.0','end').strip())
        except:
            list_[2] = float(text.get('1.0','end').strip())
        text.delete('1.0','end')
        if list_[1] == '+':
            try:
                if int(list_[2] + list_[0]) == float(list_[2] + list_[0]):
                    a = int(list_[0] + list_[2])
            except:
                a = float(list_[0] + list_[2])
            b = f'{list_[0]} + {list_[2]}'
            text.delete('1.0', 'end')
            small_text.delete('1.0', 'end')
            small_text.insert('end', b, "right")
            text.insert('end', str(a), "right")
            list_ = ['','','']
        elif list_[1] == '-':
            a = list_[0] - list_[2]
            b = f'{list_[0]} - {list_[2]}'
            text.delete('1.0', 'end')
            small_text.delete('1.0', 'end')
            small_text.insert('end', b, "right")
            text.insert('end', str(a), "right")
            list_ = ['', '', '']
        elif list_[1] == '*':
            a = list_[0] * list_[2]
            b = f'{list_[0]} × {list_[2]}'
            text.delete('1.0', 'end')
            small_text.delete('1.0', 'end')
            small_text.insert('end', b, "right")
            text.insert('end', str(a), "right")
            list_ = ['', '', '']
        elif list_[1] == '/':
            a = list_[0] / list_[2]
            b = f'{list_[0]} ÷ {list_[2]}'
            text.delete('1.0', 'end')
            small_text.delete('1.0', 'end')
            small_text.insert('end', b, "right")
            text.insert('end', str(a), "right")
            list_ = ['', '', '']

#delete键
def del_():
    global text
    text.delete("end-2c", "end-1c")

#CE键
def ce():
    global text
    text.delete('1.0', 'end')

#C键
def c():
    global text
    global small_text
    text.delete('1.0', 'end')
    small_text.delete('1.0', 'end')

#正负键
def sign():
    global text
    if text.get('1.0') == '-':
        text.delete('1.0')
    else:
        text.insert('1.0','-',"right")

#小数点
def dot():
    global text
    if "." not in text.get("1.0","end"):
        text.insert('end-1c','.',"right")

#创建按钮及文本框
def chushi():
    global small_text
    global text
    global b_1
    global b_2
    global b_3
    global b_4
    global b_5
    global b_6
    global b_7
    global b_8
    global b_9
    global b_0
    global b_dot
    global b_sign
    global b_add
    global b_minus
    global b_multi
    global b_divi
    global b_equal
    global b_del
    global b_ce
    global b_c
    small_text = Text(window,height=1, width=50)
    text = Text(window,font=("Arial", 30),height=1, width=16)
    text.tag_config("right", justify="right")
    small_text.tag_config("right", justify="right")
    b_1 = Button(window,
                     text="1",
                     padding=(30, 16),
                     bootstyle=(SUCCESS, OUTLINE),
                     command=lambda: charu('1'))
    b_2 = Button(window,
                     text="2",
                     padding=(30, 16),
                     bootstyle=(SUCCESS, OUTLINE),
                     command=lambda: charu('2'))
    b_3 = Button(window,
                     text="3",
                     padding=(30, 16),
                     bootstyle=(SUCCESS, OUTLINE),
                     command=lambda: charu('3'))
    b_4 = Button(window,
                     text="4",
                     padding=(30, 16),
                     bootstyle=(SUCCESS, OUTLINE),
                     command=lambda: charu('4'))
    b_5 = Button(window,
                     text="5",
                     padding=(30, 16),
                     bootstyle=(SUCCESS, OUTLINE),
                     command=lambda: charu('5'))
    b_6 = Button(window,
                     text="6",
                     padding=(30, 16),
                     bootstyle=(SUCCESS, OUTLINE),
                     command=lambda: charu('6'))
    b_7 = Button(window,
                     text="7",
                     padding=(30, 16),
                     bootstyle=(SUCCESS, OUTLINE),
                     command=lambda: charu('7'))
    b_8 = Button(window,
                     text="8",
                     padding=(30, 16),
                     bootstyle=(SUCCESS, OUTLINE),
                     command=lambda: charu('8'))
    b_9 = Button(window,
                     text="9",
                     padding=(30, 16),
                     bootstyle=(SUCCESS, OUTLINE),
                     command=lambda: charu('9'))
    b_0 = Button(window,
                     text="0",
                     padding=(30, 16),
                     bootstyle=(SUCCESS, OUTLINE),
                     command=lambda: charu('0'))
    b_dot = Button(window,
                       text=".",
                       padding=(32, 16),
                       bootstyle=(SUCCESS, OUTLINE),
                       command=dot)
    b_sign = Button(window,
                        text="+/-",
                        padding=(24, 16),
                        bootstyle=(SUCCESS, OUTLINE),
                        command=sign)
    b_add = Button(window,
                       text="+",
                       padding=(30, 16),
                       bootstyle=(SUCCESS, OUTLINE),
                       command=lambda: operation('+'))
    b_minus = Button(window,
                         text="-",
                         padding=(32, 16),
                         bootstyle=(SUCCESS, OUTLINE),
                         command=lambda: operation('-'))
    b_multi = Button(window,
                         text="×",
                         padding=(30, 16),
                         bootstyle=(SUCCESS, OUTLINE),
                         command = lambda: operation('*'))
    b_divi = Button(window,
                        text="÷",
                        padding=(30, 16),
                        bootstyle=(SUCCESS, OUTLINE),
                        command = lambda: operation('/'))
    b_equal = Button(window,
                         text="=",
                         padding=(30, 16),
                         bootstyle=(SUCCESS, OUTLINE),
                         command=equal)
    b_del = Button(window,
                       text="del",
                       padding=(25, 16),
                       bootstyle=(SUCCESS, OUTLINE),
                       command=del_)
    b_ce = Button(window,
                      text="CE",
                      padding=(26, 16),
                      bootstyle=(SUCCESS, OUTLINE),
                      command=ce)
    b_c = Button(window,
                     text="C",
                     padding=(30, 16),
                     bootstyle=(SUCCESS, OUTLINE),
                     command=c)
    b_0.place(x=110,y=370)
    b_1.place(x=20,y=310)
    b_2.place(x=110,y=310)
    b_3.place(x=200,y=310)
    b_4.place(x=20,y=250)
    b_5.place(x=110,y=250)
    b_6.place(x=200,y=250)
    b_7.place(x=20,y=190)
    b_8.place(x=110,y=190)
    b_9.place(x=200,y=190)
    b_dot.place(x=200,y=370)
    b_sign.place(x=20,y=370)
    b_add.place(x=290,y=310)
    b_minus.place(x=290,y=250)
    b_multi.place(x=290,y=190)
    b_divi.place(x=290, y=130)
    b_equal.place(x=290, y=370)
    b_del.place(x=200, y=130)
    b_ce.place(x=110, y=130)
    b_c.place(x=20, y=130)
    small_text.place(x=15,y=15)
    text.place(x=15,y=45)

#运行
chushi()
window.mainloop()