def page_3():
    import tkinter as tk    
        
    rec = tk.Tk()
    rec.title("剩菜小幫手")  # 此應用程式的名字
    rec.geometry('1500x750')

    l=tk.Label(rec ,bg='RosyBrown' ,width=55 ,height=2 ,font=('Courier New', 30) ,text='想要看到甚麼樣的食譜呢?' )
    l.pack()

    botton1=tk.Radiobutton(rec ,height=1 ,font = ('Courier New', 20) ,text='越夯越好' ,indicatoron=False)
    botton1.pack()
    botton2=tk.Radiobutton(rec ,height=1 ,font = ('Courier New', 20) ,text='快速上菜' ,indicatoron=False)
    botton2.pack()
    botton3=tk.Radiobutton(rec ,height=1 ,font = ('Courier New', 20), text='最新食譜', indicatoron=False)
    botton3.pack()

    rec = recipe()
    rec.master.title("剩菜小幫手")  # 此應用程式的名字

    rec.mainloop() 

def page_2():
    import tkinter as tk    
        
    rec = tk.Tk()
    rec.title("剩菜小幫手")  # 此應用程式的名字
    rec.geometry('1500x750')


    l_f=tk.Label(rec ,bg='MediumAquamarine' ,width=25 ,height=2 ,font=('Courier New', 30) ,text='要消耗的食材' )
    l_f.place(x=30, y=0)
    l_r=tk.Label(rec ,bg='MediumAquamarine' ,width=25 ,height=2 ,font=('Courier New', 30) ,text='不吃的食材' )
    l_r.place(x=650, y=0)

    """
    blank
    """
    dish1 = tk.Entry(rec, show=None, font=('Courier New', 18), width=25)
    dish1.place(x=130, y=200)
    dish2 = tk.Entry(rec, show=None, font=('Courier New', 18), width=25)
    dish2.place(x=130, y=300)
    dish3 = tk.Entry(rec, show=None, font=('Courier New', 18), width=25)
    dish3.place(x=130, y=400)

    dish1 = tk.Entry(rec, show=None, font=('Courier New', 18), width=25)
    dish1.place(x=770, y=200)
    dish2 = tk.Entry(rec, show=None, font=('Courier New', 18), width=25)
    dish2.place(x=770, y=300)
    dish3 = tk.Entry(rec, show=None, font=('Courier New', 18), width=25)
    dish3.place(x=770, y=400)
    """
    換頁
    """
    nextpagebtn = tk.Button(rec, text="下一步", width=25 ,height=1, font=('Courier New', 18), command=page_3)
    nextpagebtn.place(x=450, y=500)
    
    rec.mainloop()

page_2()