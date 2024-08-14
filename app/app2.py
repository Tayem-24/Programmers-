from tkinter import *

app = Tk()

app.title('log_in')
app.geometry("380x280+400+200")
app.resizable(False ,False)
logo = PhotoImage(file = 'pic/images.png' )
logo_lab =Label(app, image=logo)
logo_lab.place(x=70,y=10)

log_in_but = Button(app, text='log_in'
                    ,fg='black',
                    width='12',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    

                     ) 
log_in_but.place(x=70, y=233)
sigh_up_but = Button(app, text='sigh_up'
                    ,fg='black',
                    width='12',
                    bg='white',
                    cursor='hand2',
                    bd=1,
                    relief=SOLID,
                    

                     ) 
sigh_up_but.place(x=210, y=233)


app.mainloop()