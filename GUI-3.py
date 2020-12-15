import tkinter as tk
import tkinter.font as tkFont

master = tk.Tk()
v = tk.IntVar()

class recipe(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f1 = tkFont.Font(size = 30, family = 'Courier New')
        f2 = tkFont.Font(size = 20, family = 'Courier New')
        l=tk.Label(self ,bg='RosyBrown' ,width=55 ,height=2 ,font=f1 ,text='想要看到甚麼樣的食譜呢?' )
        l.pack()

        botton1=tk.Radiobutton(self ,height=1 ,font = f2 ,text='越夯越好' ,indicatoron=False)
        botton1.pack()
        botton2=tk.Radiobutton(self ,height=1 ,font = f2 ,text='快速上菜' ,indicatoron=False)
        botton2.pack()
        botton3=tk.Radiobutton(self ,height=1 ,font = f2, text='最新食譜', indicatoron=False)
        botton3.pack()

rec = recipe()
rec.master.title("剩菜小幫手")  # 此應用程式的名字
 
rec.mainloop()