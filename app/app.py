import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome!")
        root.destroy()
        show_dashboard()
    else:
        messagebox.showerror("Error", "Invalid username or password")

def signup():
    username = username_entry.get()
    password = password_entry.get()
    if username == "" or password == "":
        messagebox.showerror("Error", "Please fill all fields")
    else:
        messagebox.showinfo("Signup Successful", "Account created successfully!")
        root.destroy()
        show_dashboard()

def show_dashboard():
    global dashboard
    dashboard = tk.Tk()
    dashboard.title("Dashboard")
    dashboard.geometry("800x600")

    # Dashboard Menu
    menu = tk.Menu(dashboard)
    dashboard.config(menu=menu)
    filemenu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Exit", command=dashboard.quit)

    # Welcome Message
    welcome_label = tk.Label(dashboard, text="Welcome to Habio!", font=("Arial", 24))
    welcome_label.pack(pady=20)

    # Dashboard Content
    content_frame = tk.Frame(dashboard)
    content_frame.pack()

    # Community Tab
    community_frame = tk.Frame(content_frame)
    community_frame.pack(side=tk.LEFT, padx=20)
    community_label = tk.Label(community_frame, text="Community", font=("Arial", 18))
    community_label.pack(pady=10)

    # Life Coach Tab
    life_coach_frame = tk.Frame(content_frame)
    life_coach_frame.pack(side=tk.LEFT, padx=20)
    life_coach_label = tk.Label(life_coach_frame, text="Life Coach", font=("Arial", 18))
    life_coach_label.pack(pady=10)

    # Plans Tab
    plans_frame = tk.Frame(content_frame)
    plans_frame.pack(side=tk.LEFT, padx=20)
    plans_label = tk.Label(plans_frame, text="Plans", font=("Arial", 18))
    plans_label.pack(pady=10)

    # Set Routine Tab
    routine_frame = tk.Frame(content_frame)
    routine_frame.pack(side=tk.LEFT, padx=20)
    routine_label = tk.Label(routine_frame, text="Set Routine", font=("Arial", 18))
    routine_label.pack(pady=10)

    # Videos Tab
    videos_frame = tk.Frame(content_frame)
    videos_frame.pack(side=tk.LEFT, padx=20)
    videos_label = tk.Label(videos_frame, text="Videos", font=("Arial", 18))
    videos_label.pack(pady=10)

    dashboard.mainloop()

def main():
    global root
    root = tk.Tk()
    root.title("Habio: Your Daily Friend")
    root.geometry("800x600")

    # Login/Signup Frame
    login_signup_frame = tk.Frame(root)
    login_signup_frame.pack(pady=20)

    # Login Frame
    login_frame = tk.Frame(login_signup_frame)
    login_frame.pack(side=tk.LEFT, padx=20)
    login_label = tk.Label(login_frame, text="Login", font=("Arial", 18))
    login_label.pack()
    global username_entry
    global password_entry
    username_entry = tk.Entry(login_frame, width=25)
    username_entry.pack(pady=5)
    password_entry = tk.Entry(login_frame, width=25, show="*")
    password_entry.pack(pady=5)
    login_button = tk.Button(login_frame, text="Log In", command=login)
    login_button.pack()

    # Signup Frame
    signup_frame = tk.Frame(login_signup_frame)
    signup_frame.pack(side=tk.LEFT, padx=20)
    signup_label = tk.Label(signup_frame, text="Sign Up", font=("Arial", 18))
    signup_label.pack()
    username_entry = tk.Entry(signup_frame, width=25)
    username_entry.pack(pady=5)
    password_entry = tk.Entry(signup_frame, width=25, show="*")
    password_entry.pack(pady=5)
    signup_button = tk.Button(signup_frame, text="Sign Up", command=signup)
    signup_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()