from tkinter import *
import tkinter as tk
app = tk.Tk()
home_screen = tk.Toplevel(app)
home_screen.title("home")
home_screen.withdraw()
commu = tk.Toplevel(app)
coach = tk.Toplevel(app)
habits = tk.Toplevel(app)
videos = tk.Tk()
habits.state('withdrawn')
videos.state('withdrawn')
coach.state('withdrawn')
commu.state('withdrawn')

#=======================photo===================
#bg = PhotoImage(file="pic/cb4572f19ab7505d552206ed5dfb3739.png")
#resized_bg = bg.subsample(8,8)
#background = Label(coach, image=resized_bg)
#background.place(x=40,y=100)

#bg2 = PhotoImage(file="pic/cb4572f19ab7505d552206ed5dfb3739.png")
#resized_bg2 = bg2.subsample(7,7)
#background2 = Label(coach, image=resized_bg2)
##background2.place(x=40,y=190)

#bg3 = PhotoImage(file="pic/cb4572f19ab7505d552206ed5dfb3739.png")
#resized_bg3 = bg3.subsample(7,7)
#background3 = Label(coach, image=resized_bg3)
#background3.place(x=40,y=280)

#bg4 = PhotoImage(file="pic/cb4572f19ab7505d552206ed5dfb3739.png")
#resized_bg4 = bg4.subsample(7,7)
#background4 = Label(coach, image=resized_bg4)
#background4.place(x=40,y=370)


def info_sign():
    global name
    global password
    name = User_name.get()
    password = User_password.get()
    home()

def close_window():
    home_screen.withdraw()


def community_tab():
    commu.deiconify()
    close_window()


def habits_tab():
    habits.deiconify()
    back = Button(habits, text="Back", fg='black',
                  height='1',
                  width='5',
                  bg='white',
                  cursor='hand2',
                  bd=1,
                  relief=SOLID,
                  font=('Arial', 10, 'bold'),
                  command=backbutton)
    back.place(x=120,y=500)
    home_screen.withdraw()




def lifecoach_tab():
    #=========يظهر الشاشه=========
    coach.deiconify()
    back = Button(coach, text="Back",fg='black',
                    height='1',
                    width='5',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),
                    command=backbutton)
    back.place(x=120,y=500)
    coach.title("life choices")
    coach.geometry("360x640")
    coach.configure(bg="#f0f0f0")
    f2=Frame(coach,bg='black',bd=0 ,relief=SOLID, height=21)
    f2.place(x=1 ,y=1,width='800',height='50'  )
    #==========lable============
    l4=Label(coach,text='life choices',fg='red',bg='white',font=('times for romans', 20, 'bold'))
    l4.place(x=110,y=10)
    l5=Label(coach,text='take to the choices (mr......)',fg='red',bg='white',font=('times for romans', 10, 'bold'))
    l5.place(x=120,y=105)
    l5=Label(coach,text='take to the choices (mr......)',fg='red',bg='white',font=('times for romans', 10, 'bold'))
    l5.place(x=120,y=195)
    l5=Label(coach,text='take to the choices (mr......)',fg='red',bg='white',font=('times for romans', 10, 'bold'))
    l5.place(x=120,y=285)
    l5=Label(coach,text='take to the choices (mr......)',fg='red',bg='white',font=('times for romans', 10, 'bold'))
    l5.place(x=120,y=375)
    #========== input text =============
    e2=Entry(coach,width='20', fg='black',font=('times for romans', 10, 'bold'))
    e2.place(x=120,y=130)
    e2=Entry(coach,width='20', fg='black',font=('times for romans', 10, 'bold'))
    e2.place(x=120,y=220)
    e2=Entry(coach,width='20', fg='black',font=('times for romans', 10, 'bold'))
    e2.place(x=120,y=310)
    e2=Entry(coach,width='20', fg='black',font=('times for romans', 10, 'bold'))
    e2.place(x=120,y=400)
    #==============BUTTON===============
    b1=Button(coach, text='TXET'
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
    b2=Button(coach, text='TXET'
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
                    
    b3=Button(coach, text='TXET'
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
    b4=Button(coach, text='TXET'
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
    close_window()


def backbutton():
    commu.withdraw()
    coach.withdraw()
    videos.withdraw()
    habits.withdraw()
    home_screen.deiconify()


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
    back=Button(app, text='Back')

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
    b4 = Button(home_screen, text='Add Habits'
                , fg='black',
                height='2',
                width='10',
                bg='white',
                cursor='hand2',
                bd=1,
                relief=SOLID,
                font=('Arial', 10, 'bold'),
                command=habits_tab)
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

# logo = PhotoImage(file = 'pic/images.png' )
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