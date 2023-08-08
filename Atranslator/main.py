# import tkinter
#
# window = tkinter.Tk()    #tkinter函数创建界面
#
# window.minsize(366,366)
# window.maxsize(566,566)
# window.mainloop()  #  注册调用管理器来响应事件，即启动窗口

# import tkinter
# def main():
#     win = tkinter.Tk()
#     win.minsize(366,366)
#     win.maxsize(888,888)
#     frame_one = tkinter.Frame(win) #using Frame widget
#     area_one = tkinter.Label(frame_one,text = 'This is area_one',font=("华文行楷",20),fg="red")
#     area_one.pack(side= 'top')
#
#     area_two = tkinter.Label(frame_one, text='This is area_two', font=("黑体",20), fg="blue")
#     area_two.pack(side= 'bottom')
#
#     frame_one.pack(side='left')
#     ##
#     frame_two = tkinter.Frame(win)
#     area_one = tkinter.Label(frame_two, text='This is area_one', font=("华文行楷", 20), fg="red")
#     area_one.pack(side='top')
#
#     area_two = tkinter.Label(frame_two, text='This is area_two', font=("黑体", 20), fg="blue")
#     area_two.pack(side='bottom')
#
#     frame_two.pack(side='right')
#
#     win.mainloop()
#
# if __name__ == '__main__':
#     main()


import tkinter
import tkinter.messagebox
win = tkinter.Tk()
win.minsize(166,40)
def button_event():
    tkinter.messagebox.showinfo("Button event","welcome to Python tutorial")
button_one = tkinter.Button(win,text = "www.baidu.com",command=button_event)
button_one.pack()
win.mainloop()