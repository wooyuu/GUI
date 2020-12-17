try:
    import Tkinter as tk
except:
    import tkinter as tk
    
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        """
        p.2內容
        """
        l_f=tk.Label(self ,bg='MediumAquamarine' ,width=25 ,height=2 ,font=('Courier New', 30) ,text='要消耗的食材' )
        l_f.place(x=30, y=0)
        l_r=tk.Label(self ,bg='MediumAquamarine' ,width=25 ,height=2 ,font=('Courier New', 30) ,text='不吃的食材' )
        l_r.place(x=650, y=0)

        
        # blank
        dish1 = tk.Entry(self, show=None, font=('Courier New', 18), width=25)
        dish1.place(x=130, y=200)
        dish2 = tk.Entry(self, show=None, font=('Courier New', 18), width=25)
        dish2.place(x=130, y=300)
        dish3 = tk.Entry(self, show=None, font=('Courier New', 18), width=25)
        dish3.place(x=130, y=400)

        dish1 = tk.Entry(self, show=None, font=('Courier New', 18), width=25)
        dish1.place(x=770, y=200)
        dish2 = tk.Entry(self, show=None, font=('Courier New', 18), width=25)
        dish2.place(x=770, y=300)
        dish3 = tk.Entry(self, show=None, font=('Courier New', 18), width=25)
        dish3.place(x=770, y=400)

        tk.Button(self, text="Go to page three",
                  command=lambda: master.switch_frame(PageThree)).pack()

class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        """
        p.3內容
        """
        l=tk.Label(self ,bg='RosyBrown' ,width=55 ,height=2 ,font=('Courier New', 30) ,text='想要看到甚麼樣的食譜呢?' )
        l.pack()

        botton1=tk.Radiobutton(self ,height=1 ,font = ('Courier New', 20) ,text='越夯越好' ,indicatoron=False)
        botton1.pack()
        botton2=tk.Radiobutton(self ,height=1 ,font = ('Courier New', 20) ,text='快速上菜' ,indicatoron=False)
        botton2.pack()
        botton3=tk.Radiobutton(self ,height=1 ,font = ('Courier New', 20), text='最新食譜', indicatoron=False)
        botton3.pack()   
        
        tk.Button(self, text="Go back to page2",
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()