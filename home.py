from tkinter import *
app2 = Tk()
app2.state('withdrawn')


def home():
    app2.state('normal')
    app2.title("Home")
    app2.geometry("400x400")
    app2.configure(bg="#f0f0f0")
    f2=Frame(app2,bg='black',bd=0 ,relief=SOLID, height=21)
    f2.place(x=1 ,y=1,width='800',height='50'  )
    l4=Label(f2,text='Home',fg='red',bg='white',font=('times for romans', 20, 'bold'))
    l4.place(x=160,y=10)
    b1=Button(app2, text='hh'
                    ,fg='black',
                    height='2',
                    width='5',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),)
                    #command=hide)
    b1.place(x=175,y=60)
    b2=Button(app2, text='c'
                    ,fg='black',
                    height='2',
                    width='5',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),)
                    #command=hide)
    b2.place(x=175,y=160)
                    
    b3=Button(app2, text='v'
                    ,fg='black',
                    height='2',
                    width='5',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),)
                    #command=hide)
    b3.place(x=175,y=260)
    b4=Button(app2, text='l'
                    ,fg='black',
                    height='2',
                    width='5',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),)
                    #command=hide)
    b4.place(x=175,y=350)
home()
app2.mainloop()