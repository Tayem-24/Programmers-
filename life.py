from tkinter import *
app3 = Tk()
###=========يخفي الصفه========
app3.state('withdrawn')

#=======================photo===================
bg = PhotoImage(file="pic/cb4572f19ab7505d552206ed5dfb3739.png")
resized_bg = bg.subsample(8,8)
background = Label(app3, image=resized_bg)
background.place(x=40,y=100)

bg2 = PhotoImage(file="pic/cb4572f19ab7505d552206ed5dfb3739.png")
resized_bg2 = bg2.subsample(7,7)
background2 = Label(app3, image=resized_bg)
background2.place(x=40,y=190)

bg3 = PhotoImage(file="pic/cb4572f19ab7505d552206ed5dfb3739.png")
resized_bg3 = bg3.subsample(7,7)
background3 = Label(app3, image=resized_bg)
background3.place(x=40,y=280)

bg4 = PhotoImage(file="pic/cb4572f19ab7505d552206ed5dfb3739.png")
resized_bg4 = bg4.subsample(7,7)
background4 = Label(app3, image=resized_bg)
background4.place(x=40,y=370)

def life1():
    #=========يظهر الشاشه=========
    app3.state('normal')

    app3.title("life choices")
    app3.geometry("360x640")
    app3.configure(bg="#f0f0f0")
    f2=Frame(app3,bg='black',bd=0 ,relief=SOLID, height=21)
    f2.place(x=1 ,y=1,width='800',height='50'  )
    #==========lable============
    l4=Label(app3,text='life choices',fg='red',bg='white',font=('times for romans', 20, 'bold'))
    l4.place(x=110,y=10)
    l5=Label(app3,text='take to the choices (mr......)',fg='red',bg='white',font=('times for romans', 10, 'bold'))
    l5.place(x=120,y=105)
    l5=Label(app3,text='take to the choices (mr......)',fg='red',bg='white',font=('times for romans', 10, 'bold'))
    l5.place(x=120,y=195)
    l5=Label(app3,text='take to the choices (mr......)',fg='red',bg='white',font=('times for romans', 10, 'bold'))
    l5.place(x=120,y=285)
    l5=Label(app3,text='take to the choices (mr......)',fg='red',bg='white',font=('times for romans', 10, 'bold'))
    l5.place(x=120,y=375)
    #========== input text =============
    e2=Entry(app3,width='20', fg='black',font=('times for romans', 10, 'bold'))
    e2.place(x=120,y=130)
    e2=Entry(app3,width='20', fg='black',font=('times for romans', 10, 'bold'))
    e2.place(x=120,y=220)
    e2=Entry(app3,width='20', fg='black',font=('times for romans', 10, 'bold'))
    e2.place(x=120,y=310)
    e2=Entry(app3,width='20', fg='black',font=('times for romans', 10, 'bold'))
    e2.place(x=120,y=400)
    #==========ر====================
    b1=Button(app3, text='TXET'
                    ,fg='black',
                    height='1',
                    width='5',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),)
                    #command=hide)
    b1.place(x=120,y=150)
    b2=Button(app3, text='TXET'
                    ,fg='black',
                    height='1',
                    width='5',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),)
                    #command=hide)
    b2.place(x=120,y=240)
                    
    b3=Button(app3, text='TXET'
                    ,fg='black',
                    height='1',
                    width='5',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),)
                    #command=hide)
    b3.place(x=120,y=330)
    b4=Button(app3, text='TXET'
                    ,fg='black',
                    height='1',
                    width='5',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),)
                    #command=hide)
    b4.place(x=120,y=420)







life1()






#logo2 = PhotoImage(file = 'pic/cb4572f19ab7505d552206ed5dfb3739.png' )
#logo_lab =Label(app3, image=logo2)
#logo_lab = logo2.subsample(2,2)
#logo_lab.place(x=70,y=10)

app3.mainloop()