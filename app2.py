from tkinter import *

# Initialize main window
app = Tk()
app.geometry("500x500+400+200")
app.title("Application")
app.resizable(False, False)

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Function to handle login action
def login():
    # Here you can add logic to check username and password
    # For this example, we will just switch to the home frame
    show_frame(home_frame)

# Create all the frames
login_frame = Frame(app, bg="#D1C4E9")  # Light purple background
home_frame = Frame(app, bg="#D1C4E9")
plan_frame = Frame(app, bg="#D1C4E9")
welcome_frame = Frame(app, bg="#D1C4E9")

for frame in (login_frame, home_frame, plan_frame, welcome_frame):
    frame.place(x=0, y=0, width=500, height=500)

# Add content to the login frame
Label(login_frame, text="LOG IN", font=("Arial", 24, "bold"), bg="#D1C4E9", fg="#6A1B9A").pack(pady=20)
Label(login_frame, text="Email", font=("Arial", 14), bg="#D1C4E9").pack(pady=10)
Entry(login_frame, font=("Arial", 14)).pack(pady=5)
Label(login_frame, text="Password", font=("Arial", 14), bg="#D1C4E9").pack(pady=10)
Entry(login_frame, font=("Arial", 14), show="*").pack(pady=5)
Button(login_frame, text="Log In", font=("Arial", 14), command=login).pack(pady=20)

# Add content to the home frame
Label(home_frame, text="Home", font=("Arial", 24, "bold"), bg="#D1C4E9", fg="#6A1B9A").pack(pady=20)
# Add more widgets as needed for the home screen

# Show the login frame initially
show_frame(login_frame)

app.mainloop()



from tkinter import *

# Initialize main window
app = Tk()
app.geometry("500x500+400+200")
app.title("Application")
app.resizable(False, False)

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Function to handle login action
def login():
    # Here you can add logic to check username and password
    # For this example, we will just switch to the home frame
    show_frame(home_frame)

# Create all the frames
login_frame = Frame(app, bg="#D1C4E9")  # Light purple background
home_frame = Frame(app, bg="#D1C4E9")
plan_frame = Frame(app, bg="#D1C4E9")
welcome_frame = Frame(app, bg="#D1C4E9")

for frame in (login_frame, home_frame, plan_frame, welcome_frame):
    frame.place(x=0, y=0, width=500, height=500)

# Add content to the login frame
Label(login_frame, text="LOG IN", font=("Arial", 24, "bold"), bg="#D1C4E9", fg="#6A1B9A").pack(pady=20)
Label(login_frame, text="Email", font=("Arial", 14), bg="#D1C4E9").pack(pady=10)
Entry(login_frame, font=("Arial", 14)).pack(pady=5)
Label(login_frame, text="Password", font=("Arial", 14), bg="#D1C4E9").pack(pady=10)
Entry(login_frame, font=("Arial", 14), show="*").pack(pady=5)
Button(login_frame, text="Log In", font=("Arial", 14), command=login).pack(pady=20)

# Add content to the home frame
Label(home_frame, text="Home", font=("Arial", 24, "bold"), bg="#D1C4E9", fg="#6A1B9A").pack(pady=20)
# Add more widgets as needed for the home screen

# Show the login frame initially
show_frame(login_frame)

app.mainloop()





from tkinter import *
from PIL import Image, ImageTk

# Initialize main window
app = Tk()
app.geometry("500x500+400+200")
app.title("Application")
app.resizable(False, False)

# Load the background image
bg_image = Image.open("3ec394ae-a7f8-4bba-a85d-fbdb6a2256df.png")  # استبدل "background.png" بمسار الصورة
bg_image = bg_image.resize((500, 500), Image.ANTIALIAS)  # ضبط حجم الصورة على حجم النافذة
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Label to hold the image and place it
bg_label = Label(app, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Create all the frames
login_frame = Frame(app, bg="#D1C4E9")  # Light purple background
signup_frame = Frame(app, bg="#D1C4E9")
home_frame = Frame(app, bg="#D1C4E9")
plan_frame = Frame(app, bg="#D1C4E9")
welcome_frame = Frame(app, bg="#D1C4E9")

for frame in (login_frame, signup_frame, home_frame, plan_frame, welcome_frame):
    frame.place(x=0, y=0, width=500, height=500)

# Add content to the login frame (example)
Label(login_frame, text="LOG IN", font=("Arial", 24, "bold"), bg="#D1C4E9", fg="#6A1B9A").pack(pady=20)

# Show the login frame initially
show_frame(login_frame)

app.mainloop()




from tkinter import *

# Initialize main window
app = Tk()
app.geometry("500x500+400+200")
app.title("Application")
app.config(background="#E0E0E0")  
app.resizable(False, False)


def show_frame(frame):
    frame.tkraise()


login_frame = Frame(app, bg="#D1C4E9")  
signup_frame = Frame(app, bg="#D1C4E9")
home_frame = Frame(app, bg="#D1C4E9")
plan_frame = Frame(app, bg="#D1C4E9")
welcome_frame = Frame(app, bg="#D1C4E9")

for frame in (login_frame, signup_frame, home_frame, plan_frame, welcome_frame):
    frame.place(x=0, y=0, width=500, height=500)


Label(login_frame, text="LOG IN", font=("Arial", 24, "bold"), bg="#D1C4E9", fg="#6A1B9A").pack(pady=20)  
Label(login_frame, text="Email", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(login_frame, font=("Arial", 14), bg="#B39DDB", fg="black").pack(pady=10)

Label(login_frame, text="Password", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(login_frame, font=("Arial", 14), show="*", bg="#B39DDB", fg="black").pack(pady=10)

Button(login_frame, text="LOG IN", font=("Arial", 14), bg="#8E24AA", fg="white").pack(pady=20)
Button(login_frame, text="Sign up", font=("Arial", 12), bg="#D1C4E9", fg="#6A1B9A", command=lambda: show_frame(signup_frame)).pack()


Label(signup_frame, text="SIGN UP", font=("Arial", 24, "bold"), bg="#D1C4E9", fg="#6A1B9A").pack(pady=20)
Label(signup_frame, text="Name", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(signup_frame, font=("Arial", 14), bg="#B39DDB", fg="black").pack(pady=10)

Label(signup_frame, text="Email", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(signup_frame, font=("Arial", 14), bg="#B39DDB", fg="black").pack(pady=10)

Label(signup_frame, text="Password", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(signup_frame, font=("Arial", 14), show="*", bg="#B39DDB", fg="black").pack(pady=10)

Button(signup_frame, text="Sign up", font=("Arial", 14), bg="#8E24AA", fg="white").pack(pady=20)
Button(signup_frame, text="Log in", font=("Arial", 12), bg="#D1C4E9", fg="#6A1B9A", command=lambda: show_frame(login_frame)).pack()


Label(home_frame, text="Home", font=("Arial", 24, "bold"), bg="#D1C4E9", fg="#6A1B9A").pack(pady=20)
for i in range(4):
    Label(home_frame, text=f"Option {i+1}", font=("Arial", 14), bg="#9575CD", fg="white").pack(pady=10)  

Button(home_frame, text="Create Plan", font=("Arial", 14), bg="#8E24AA", fg="white", command=lambda: show_frame(plan_frame)).pack(pady=20)
Button(home_frame, text="Welcome Video", font=("Arial", 14), bg="#8E24AA", fg="white", command=lambda: show_frame(welcome_frame)).pack(pady=20)


Label(plan_frame, text="Make Your Own Plan", font=("Arial", 24, "bold"), bg="#D1C4E9", fg="#6A1B9A").pack(pady=20)
Label(plan_frame, text="When do you wake up?", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(plan_frame, font=("Arial", 14), bg="#B39DDB", fg="black").pack(pady=10)

Label(plan_frame, text="When do you go to sleep?", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(plan_frame, font=("Arial", 14), bg="#B39DDB", fg="black").pack(pady=10)

Label(plan_frame, text="What are your working hours?", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(plan_frame, font=("Arial", 14), bg="#B39DDB", fg="black").pack(pady=10)

Label(plan_frame, text="What are your daily habits?", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(plan_frame, font=("Arial", 14), bg="#B39DDB", fg="black").pack(pady=10)

Button(plan_frame, text="Next", font=("Arial", 14), bg="#8E24AA", fg="white").pack(pady=20)


Label(welcome_frame, text="Welcome", font=("Arial", 24, "bold"), bg="#D1C4E9", fg="#6A1B9A").pack(pady=20)
Label(welcome_frame, text="Introduction Video", font=("Arial", 18), bg="#D1C4E9", fg="#6A1B9A").pack(pady=10)
Label(welcome_frame, text="(Video Placeholder)", font=("Arial", 14), bg="#B39DDB", fg="black", width=30, height=10).pack(pady=20)


show_frame(login_frame)

app.mainloop()





from tkinter import *
from PIL import Image, ImageTk

# Initialize main window
app = Tk()
app.geometry("500x500+400+200")
app.title("Application")
app.resizable(False, False)

# Load the background image
bg_image = Image.open("background.png")  # استبدل "background.png" بمسار الصورة
bg_image = bg_image.resize((500, 500), Image.ANTIALIAS)  # ضبط حجم الصورة على حجم النافذة
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Label to hold the image and place it
bg_label = Label(app, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Create all the frames
login_frame = Frame(app, bg="#D1C4E9")  # Light purple background
signup_frame = Frame(app, bg="#D1C4E9")
home_frame = Frame(app, bg="#D1C4E9")
plan_frame = Frame(app, bg="#D1C4E9")
welcome_frame = Frame(app, bg="#D1C4E9")

for frame in (login_frame, signup_frame, home_frame, plan_frame, welcome_frame):
    frame.place(x=0, y=0, width=500, height=500)

# Add content to the login frame (example)
Label(login_frame, text="LOG IN", font=("Arial", 24, "bold"), bg="#D1C4E9", fg="#6A1B9A").pack(pady=20)

# Show the login frame initially
show_frame(login_frame)

app.mainloop()






from tkinter import *

# Initialize main window
app = Tk()
app.geometry("500x500+400+200")
app.title("Application")
app.config(background="#E0E0E0")  # Light grey background for main window
app.resizable(False, False)

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Create all the frames
login_frame = Frame(app, bg="#D1C4E9")  # Light purple background
signup_frame = Frame(app, bg="#D1C4E9")
home_frame = Frame(app, bg="#D1C4E9")
plan_frame = Frame(app, bg="#D1C4E9")
welcome_frame = Frame(app, bg="#D1C4E9")

for frame in (login_frame, signup_frame, home_frame, plan_frame, welcome_frame):
    frame.place(x=0, y=0, width=500, height=500)

# --------- Login Frame ---------
Label(login_frame, text="LOG IN", font=("Arial", 24, "bold"), bg="#D1C4E9", fg="#6A1B9A").pack(pady=20)  # Dark purple text
Label(login_frame, text="Email", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(login_frame, font=("Arial", 14), bg="#B39DDB", fg="black").pack(pady=10)

Label(login_frame, text="Password", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(login_frame, font=("Arial", 14), show="*", bg="#B39DDB", fg="black").pack(pady=10)

Button(login_frame, text="LOG IN", font=("Arial", 14), bg="#8E24AA", fg="white").pack(pady=20)
Button(login_frame, text="Sign up", font=("Arial", 12), bg="#D1C4E9", fg="#6A1B9A", command=lambda: show_frame(signup_frame)).pack()

# --------- Signup Frame ---------
Label(signup_frame, text="SIGN UP", font=("Arial", 24, "bold"), bg="#D1C4E9", fg="#6A1B9A").pack(pady=20)
Label(signup_frame, text="Name", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(signup_frame, font=("Arial", 14), bg="#B39DDB", fg="black").pack(pady=10)

Label(signup_frame, text="Email", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(signup_frame, font=("Arial", 14), bg="#B39DDB", fg="black").pack(pady=10)

Label(signup_frame, text="Password", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(signup_frame, font=("Arial", 14), show="*", bg="#B39DDB", fg="black").pack(pady=10)

Button(signup_frame, text="Sign up", font=("Arial", 14), bg="#8E24AA", fg="white").pack(pady=20)
Button(signup_frame, text="Log in", font=("Arial", 12), bg="#D1C4E9", fg="#6A1B9A", command=lambda: show_frame(login_frame)).pack()

# --------- Home Frame ---------
Label(home_frame, text="Home", font=("Arial", 24, "bold"), bg="#D1C4E9", fg="#6A1B9A").pack(pady=20)
for i in range(4):
    Label(home_frame, text=f"Option {i+1}", font=("Arial", 14), bg="#9575CD", fg="white").pack(pady=10)  # Medium purple

Button(home_frame, text="Create Plan", font=("Arial", 14), bg="#8E24AA", fg="white", command=lambda: show_frame(plan_frame)).pack(pady=20)
Button(home_frame, text="Welcome Video", font=("Arial", 14), bg="#8E24AA", fg="white", command=lambda: show_frame(welcome_frame)).pack(pady=20)

# --------- Plan Creation Frame ---------
Label(plan_frame, text="Make Your Own Plan", font=("Arial", 24, "bold"), bg="#D1C4E9", fg="#6A1B9A").pack(pady=20)
Label(plan_frame, text="When do you wake up?", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(plan_frame, font=("Arial", 14), bg="#B39DDB", fg="black").pack(pady=10)

Label(plan_frame, text="When do you go to sleep?", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(plan_frame, font=("Arial", 14), bg="#B39DDB", fg="black").pack(pady=10)

Label(plan_frame, text="What are your working hours?", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(plan_frame, font=("Arial", 14), bg="#B39DDB", fg="black").pack(pady=10)

Label(plan_frame, text="What are your daily habits?", font=("Arial", 14), bg="#D1C4E9", fg="#6A1B9A").pack()
Entry(plan_frame, font=("Arial", 14), bg="#B39DDB", fg="black").pack(pady=10)

Button(plan_frame, text="Next", font=("Arial", 14), bg="#8E24AA", fg="white").pack(pady=20)

# --------- Welcome Frame ---------
Label(welcome_frame, text="Welcome", font=("Arial", 24, "bold"), bg="#D1C4E9", fg="#6A1B9A").pack(pady=20)
Label(welcome_frame, text="Introduction Video", font=("Arial", 18), bg="#D1C4E9", fg="#6A1B9A").pack(pady=10)
Label(welcome_frame, text="(Video Placeholder)", font=("Arial", 14), bg="#B39DDB", fg="black", width=30, height=10).pack(pady=20)

# Show the login frame initially
show_frame(login_frame)

app.mainloop()




from tkinter import *

# Initialize main window
app = Tk()
app.geometry("500x500+400+200")
app.title("Application")
app.config(background="white")
app.resizable(False, False)

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Create all the frames
login_frame = Frame(app, bg="white")
signup_frame = Frame(app, bg="white")
home_frame = Frame(app, bg="white")
plan_frame = Frame(app, bg="white")
welcome_frame = Frame(app, bg="white")

for frame in (login_frame, signup_frame, home_frame, plan_frame, welcome_frame):
    frame.place(x=0, y=0, width=500, height=500)

# --------- Login Frame ---------
Label(login_frame, text="LOG IN", font=("Arial", 24), bg="white").pack(pady=20)
Label(login_frame, text="Email", font=("Arial", 14), bg="white").pack()
Entry(login_frame, font=("Arial", 14)).pack(pady=10)

Label(login_frame, text="Password", font=("Arial", 14), bg="white").pack()
Entry(login_frame, font=("Arial", 14), show="*").pack(pady=10)

Button(login_frame, text="LOG IN", font=("Arial", 14), bg="blue", fg="white").pack(pady=20)
Button(login_frame, text="Sign up", font=("Arial", 12), bg="white", fg="blue", command=lambda: show_frame(signup_frame)).pack()

# --------- Signup Frame ---------
Label(signup_frame, text="SIGN UP", font=("Arial", 24), bg="white").pack(pady=20)
Label(signup_frame, text="Name", font=("Arial", 14), bg="white").pack()
Entry(signup_frame, font=("Arial", 14)).pack(pady=10)

Label(signup_frame, text="Email", font=("Arial", 14), bg="white").pack()
Entry(signup_frame, font=("Arial", 14)).pack(pady=10)

Label(signup_frame, text="Password", font=("Arial", 14), bg="white").pack()
Entry(signup_frame, font=("Arial", 14), show="*").pack(pady=10)

Button(signup_frame, text="Sign up", font=("Arial", 14), bg="green", fg="white").pack(pady=20)
Button(signup_frame, text="Log in", font=("Arial", 12), bg="white", fg="blue", command=lambda: show_frame(login_frame)).pack()

# --------- Home Frame ---------
Label(home_frame, text="Home", font=("Arial", 24), bg="white").pack(pady=20)
for i in range(4):
    Label(home_frame, text=f"Option {i+1}", font=("Arial", 14), bg="lightblue").pack(pady=10)

Button(home_frame, text="Create Plan", font=("Arial", 14), bg="blue", fg="white", command=lambda: show_frame(plan_frame)).pack(pady=20)
Button(home_frame, text="Welcome Video", font=("Arial", 14), bg="blue", fg="white", command=lambda: show_frame(welcome_frame)).pack(pady=20)

# --------- Plan Creation Frame ---------
Label(plan_frame, text="Make Your Own Plan", font=("Arial", 24), bg="white").pack(pady=20)
Label(plan_frame, text="When do you wake up?", font=("Arial", 14), bg="white").pack()
Entry(plan_frame, font=("Arial", 14)).pack(pady=10)

Label(plan_frame, text="When do you go to sleep?", font=("Arial", 14), bg="white").pack()
Entry(plan_frame, font=("Arial", 14)).pack(pady=10)

Label(plan_frame, text="What are your working hours?", font=("Arial", 14), bg="white").pack()
Entry(plan_frame, font=("Arial", 14)).pack(pady=10)

Label(plan_frame, text="What are your daily habits?", font=("Arial", 14), bg="white").pack()
Entry(plan_frame, font=("Arial", 14)).pack(pady=10)

Button(plan_frame, text="Next", font=("Arial", 14), bg="green", fg="white").pack(pady=20)

# --------- Welcome Frame ---------
Label(welcome_frame, text="Welcome", font=("Arial", 24), bg="white").pack(pady=20)
Label(welcome_frame, text="Introduction Video", font=("Arial", 18), bg="white").pack(pady=10)
Label(welcome_frame, text="(Video Placeholder)", font=("Arial", 14), bg="grey", width=30, height=10).pack(pady=20)

# Show the login frame initially
show_frame(login_frame)

app.mainloop()




from tkinter import *

app = Tk()
app2 = Tk()
app3 = Tk()
app4 = Tk()
app5 = Tk()
app6 = Tk()
app7 = Tk()
app8 = Tk()

app2.state('withdrawn')
app3.state('withdrawn')
app4.state('withdrawn')
app5.state('withdrawn')
app6.state('withdrawn')
app7.state('withdrawn')
app8.state('withdrawn')

app.geometry("500x500+400+200")
fr = Frame(width='300' ,height=100 ,bg='white')
fr.place(x=1,y=1)
app.resizable(True ,False)
app.title("app h")
app.config(background= "black")
app.iconbitmap('Screenshot 2024-08-13 225742.ico')
app.minsize(200,200)
#app.mixsize(800,800)
bt = Button(fr, text="log in" ,fg='black' ,bg='white',cursor="heart" )
bt.place(x=1,y=2)
app2.geometry("500x500+400+200")
app2.resizable(True ,False)
app2.title("app h")
app2.config(background= "red")
app2.iconbitmap('Screenshot 2024-08-13 225742.ico')
app2.minsize(200,200)
#app2.mixsize(800,800)

app3.geometry("500x500+400+200")
app3.resizable(True ,False)
app3.title("app h")
app3.config(background= "red")
app3.iconbitmap('Screenshot 2024-08-13 225742.ico')
app3.minsize(200,200)
#app.mixsize(800,800)

app4.geometry("500x500+400+200")
app4.resizable(True ,False)
app4.title("app h")
app4.config(background= "red")
app4.iconbitmap('Screenshot 2024-08-13 225742.ico')
app4.minsize(200,200)
#app4.mixsize(800,800)

app5.geometry("500x500+400+200")
app5.resizable(True ,False)
app5.title("app h")
app5.config(background= "red")
app5.iconbitmap('Screenshot 2024-08-13 225742.ico')
app5.minsize(200,200)
#app5.mixsize(800,800)

app6.geometry("500x500+400+200")
app6.resizable(True ,False)
app6.title("app h")
app6.config(background= "red")
app6.iconbitmap('Screenshot 2024-08-13 225742.ico')
app6.minsize(200,200)
#app6.mixsize(800,800)


app7.geometry("500x500+400+200")
app7.resizable(True ,False)
app7.title("app h")
app7.config(background= "red")
app7.iconbitmap('Screenshot 2024-08-13 225742.ico')
app7.minsize(200,200)
#app7.mixsize(800,800)

app8.geometry("500x500+400+200")
app8.resizable(True ,False)
app8.title("app h")
app8.config(background= "red")
app8.iconbitmap('Screenshot 2024-08-13 225742.ico')
app8.minsize(200,200)
#app.mixsize(800,800)

app.mainloop()