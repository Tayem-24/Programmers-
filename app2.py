from tkinter import *

app = Tk()

def but1(event=None):
    log_in_but.config(background='black',foreground='white')

def lv1(event=None):
    log_in_but.config(background='white',foreground='black')

def but2(event=None):
    sigh_up_but.config(background='black',foreground='white')

def lv2(event=None):
    sigh_up_but.config(background='white',foreground='black')

def hide(event=None):
    app.geometry("350x300+400+200")

def log(event=None):
    app.geometry("630x300+400+200")
    b1=Button(app, text='<'
                    ,fg='black',
                    height='21',
                    width='12',
                    bg='white',
                    cursor='hand2',
                    bd=0,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),
                    command=hide)
    b1.place(x=610 ,y=6 )

    f1=Frame(app,bg='white',bd=0 ,relief=SOLID, height=21)
    f1.place(x=400 ,y=5,width='205',height='330'  )
    l=Label(f1,text='welcome',fg='red',bg='white',font=('times for romans', 16, 'bold'))
    l.place(x=10,y=50)
    l2=Label(f1,text='user_name',fg='red',bg='white',font=('times for romans', 12, 'bold'))
    l2.place(x=10,y=100)
    e1=Entry(f1,width='20', fg='black',font=('times for romans', 10, 'bold'))
    e1.place(x=10,y=125)

    l3=Label(f1,text='password',fg='red',bg='white',font=('times for romans', 12, 'bold'))
    l3.place(x=10,y=140)
    e2=Entry(f1,width='20', fg='black',font=('times for romans', 10, 'bold'))
    e2.place(x=10,y=160)
    b2=Button(f1, text='log_in'
                    ,fg='red',
                    height='2',
                    width='15',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),)
    b2.place(x=10 ,y=200 )
    b3=Button(f1, text='sigh_up'
                    ,fg='red',
                    height='2',
                    width='15',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),)
    b3.place(x=10 ,y=250 )
    

def sigh(event=None):
    app.geometry("630x300+400+200")
    b1=Button(app, text='<'
                    ,fg='black',
                    height='21',
                    width='12',
                    bg='white',
                    cursor='hand2',
                    bd=0,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),
                    command=hide)
    b1.place(x=610 ,y=6 )

    f1=Frame(app,bg='white',bd=0 ,relief=SOLID, height=21)
    f1.place(x=400 ,y=5,width='205',height='330'  )
    l=Label(f1,text='welcome',fg='red',bg='white',font=('times for romans', 16, 'bold'))
    l.place(x=10,y=50)
    l2=Label(f1,text='user_name',fg='red',bg='white',font=('times for romans', 12, 'bold'))
    l2.place(x=10,y=100)
    e1=Entry(f1,width='20', fg='black',font=('times for romans', 10, 'bold'))
    e1.place(x=10,y=125)

    l3=Label(f1,text='password',fg='red',bg='white',font=('times for romans', 12, 'bold'))
    l3.place(x=10,y=140)
    e2=Entry(f1,width='20', fg='black',font=('times for romans', 10, 'bold'))
    e2.place(x=10,y=160)
    b2=Button(f1, text='log_in'
                    ,fg='red',
                    height='2',
                    width='15',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),)
    b2.place(x=10 ,y=200 )
    b3=Button(f1, text='sigh_up'
                    ,fg='red',
                    height='2',
                    width='15',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),)
    b3.place(x=10 ,y=250 )



app.title('log_in')
app.geometry("350x300+400+200")
app.resizable(False ,False)
logo = PhotoImage(file = 'pic/images.png' )
log_pic = PhotoImage(file = 'pic/images1.png' )

logo_lab =Label(app, image=logo)
logo_lab.place(x=70,y=10)

log_in_but = Button(app, text='log_in'
                    ,fg='black',
                    width='12',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),
                    command=log

                     ) 
log_in_but.place(x=70, y=233)
sigh_up_but = Button(app, text='sigh_up'
                    ,fg='black',
                    width='12',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),
                    command=sigh
                     ) 
sigh_up_but.place(x=210, y=233)

log_in_but.bind('<Enter>', but1)
log_in_but.bind('<Leave>', lv1)


sigh_up_but.bind('<Enter>', but2)
sigh_up_but.bind('<Leave>', lv2)
app.mainloop()