import tkinter as tk    
    
rec = tk.Tk()
rec.title("剩菜小幫手")  # 此應用程式的名字
rec.geometry('3000x2000')

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


rec.mainloop()