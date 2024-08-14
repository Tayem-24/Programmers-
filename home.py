from tkinter import *
import tkinter as tk
home_screen = tk.Tk()
commu = tk.Tk()
coach = tk.Tk()
videos = tk.Tk()
videos.state('withdrawn')
coach.state('withdrawn')
commu.state('withdrawn')
###=========يخفي الصفه========
home_screen.state('withdrawn')


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
    


def home():
    #=========يظهر الشاشه=========
    home_screen.state('normal')

    home_screen.title("Home")
    home_screen.geometry("360x640")
    home_screen.configure(bg="#f0f0f0")
    f2=Frame(home_screen,bg='black',bd=0 ,relief=SOLID, height=21)
    f2.place(x=1 ,y=1,width='800',height='50'  )
    #==========lable============
    l4=Label(f2,text='Home',fg='red',bg='black',font=('times for romans', 20, 'bold'))
    l4.place(x=160,y=10)
    #=========button=======
    commu_button = Button(home_screen, text='Community'
                    ,fg='black',
                    height='2',
                    width='10',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),
                    command=community_tab)
    commu_button.place(x=175,y=60)
    lifecoach_button = Button(home_screen, text='Life coach'
                    ,fg='black',
                    height='2',
                    width='10',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),
                    command=lifecoach_tab)
    lifecoach_button.place(x=175,y=160)
                    
    b3=Button(home_screen, text='Videos'
                    ,fg='black',
                    height='2',
                    width='10',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),
                    command=videos_tab)
    b3.place(x=175,y=260)
    b4=Button(home_screen, text='l'
                    ,fg='black',
                    height='2',
                    width='10',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    font=('Arial', 10, 'bold'),)
                    #command=hide)
    b4.place(x=175,y=350)
home_screen.resizable(False, False)
bg = PhotoImage(file="WhatsApp Image 2024-08-14 at 00.00.38_eebab647.png")
resized_bg = bg.subsample(2,2)
background = Label(home_screen, image=resized_bg)
background.place(x=0,y=0)
home()
home_screen.mainloop()