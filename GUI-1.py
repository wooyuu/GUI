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
        f1 = tkFont.Font(size = 22, family = 'Courier New')
        f2 = tkFont.Font(size = 18, family = 'Courier New')
        l=tk.Label(self ,bg='aliceblue' ,width=75 ,height=2 ,font=f1 ,text='今晚我想來點......' )
        l.pack()

        botton1=tk.Radiobutton(self ,height=1 ,font = f2 ,text='湊一湊就上桌',indicatoron=False)
        botton1.pack()
        botton2=tk.Radiobutton(self ,height=1 ,font = f2 ,text='幫我盡可能處理掉他們 即使要付出代價',indicatoron=False)
        botton2.pack()

rec = recipe()
rec.master.title("剩菜小幫手")  # 此應用程式的名字

rec.mainloop()