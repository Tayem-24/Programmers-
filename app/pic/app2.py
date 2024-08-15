from tkinter import *
import tkinter as tk
app = tk.Tk()
home_screen = tk.Toplevel(app)
home_screen.title("home")
home_screen.withdraw()
commu = tk.Tk()
coach = tk.Tk()
videos = tk.Tk()
videos.state('withdrawn')
coach.state('withdrawn')
commu.state('withdrawn')


def info_sign():
    global name
    global password
    name = User_name.get()
    password = User_password.get()
    home()

def close_window():
    home_screen.destroy()


def community_tab():
    commu.state('normal')
    close_window()


def lifecoach_tab():
    coach.state('normal')
    home_screen.destroy()


def videos_tab():
    videos.state('normal')
    home_screen.destroy()


def but1(event=None):
    log_in_but.config(background='black',foreground='white')

def lv1(event=None):
    log_in_but.config(background='white',foreground='black')

def but2(event=None):
    sign_up_but.config(background='black',foreground='white')

def lv2(event=None):
    sign_up_but.config(background='white',foreground='black')

def hide(event=None):
    app.geometry("350x300+400+200")

def log(event=None):
    global e1
    global e2
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
    f1.place(x=400 ,y=5,width='205',height='330')
    l=Label(f1,text='log_in',fg='red',bg='white',font=('times for romans', 16, 'bold'))
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


def home():
    # =========يظهر الشاشه=========
    home_screen.deiconify()
    home_screen.title("Home")
    home_screen.geometry("360x640")
    home_screen.configure(bg="#f0f0f0")
    f2 = Frame(home_screen, bg='black', bd=0, relief=SOLID, height=21)
    f2.place(x=1, y=1, width='800', height='50')
    # ==========lable============
    l4 = Label(f2, text='Home', fg='red', bg='black', font=('times for romans', 20, 'bold'))
    l4.place(x=160, y=10)
    # =========button=======
    commu_button = Button(home_screen, text='Community'
                          , fg='black',
                          height='2',
                          width='10',
                          bg='white',
                          cursor='hand2',
                          bd=1,
                          relief=SOLID,
                          font=('Arial', 10, 'bold'),
                          command=community_tab)
    commu_button.place(x=175, y=60)
    lifecoach_button = Button(home_screen, text='Life coach'
                              , fg='black',
                              height='2',
                              width='10',
                              bg='white',
                              cursor='hand2',
                              bd=1,
                              relief=SOLID,
                              font=('Arial', 10, 'bold'),
                              command=lifecoach_tab)
    lifecoach_button.place(x=175, y=160)

    b3 = Button(home_screen, text='Videos'
                , fg='black',
                height='2',
                width='10',
                bg='white',
                cursor='hand2',
                bd=1,
                relief=SOLID,
                font=('Arial', 10, 'bold'),
                command=videos_tab)
    b3.place(x=175, y=260)
    b4 = Button(home_screen, text='l'
                , fg='black',
                height='2',
                width='10',
                bg='white',
                cursor='hand2',
                bd=1,
                relief=SOLID,
                font=('Arial', 10, 'bold'), )
    # command=hide)
    b4.place(x=175, y=350)
    app.state('withdrawn')




def sign(event=None):
    global User_name
    global User_password
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
    l=Label(f1,text='sign_up',fg='red',bg='white',font=('times for romans', 16, 'bold'))
    l.place(x=10,y=50)
    l2=Label(f1,text='user_name',fg='red',bg='white',font=('times for romans', 12, 'bold'))
    l2.place(x=10,y=100)
    User_name = Entry(f1,width='20', fg='black',font=('times for romans', 10, 'bold'))
    User_name.place(x=10,y=125)

    l3=Label(f1,text='password',fg='red',bg='white',font=('times for romans', 12, 'bold'))
    l3.place(x=10,y=140)
    User_password=Entry(f1,width='20', fg='black',show='*',font=('times for romans', 10, 'bold'))
    User_password.place(x=10,y=160)

    b3=Button(f1, text='sign_up'
                    ,fg='red',
                    height='2',
                    width='15',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),
                    command=info_sign)
    b3.place(x=10 ,y=200 )



app.title('log_in')
app.geometry("350x300+400+200")
app.resizable(False ,False)
# logo = PhotoImage(file = 'C:/Users/tayem/Documents/GitHub/Programmers-/app/pic/Login_image.png' )
# log_pic = PhotoImage(file = 'pic/images1.png' )

# logo_lab =Label(app, image=logo)
# logo_lab.place(x=70,y=10)
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
sign_up_but = Button(app, text='sign_up'
                    ,fg='black',
                    width='12',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),
                    command=sign
                     ) 
sign_up_but.place(x=210, y=233)

log_in_but.bind('<Enter>', but1)
log_in_but.bind('<Leave>', lv1)


sign_up_but.bind('<Enter>', but2)
sign_up_but.bind('<Leave>', lv2)
app.mainloop()