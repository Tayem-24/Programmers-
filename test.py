import tkinter as tk

# Create the main application window
app = tk.Tk()
app.title("Entry Example")
app.geometry("300x200")

# Assign the Entry widget to a variable
user_entry = tk.Entry(app, width=20)
user_entry.pack(pady=20)

# Function to get the text from the Entry widget using the variable
def get_entry_text():
    user_input = user_entry.get()  # Use the variable to call .get()
    print(f"User entered: {user_input}")

# Create a Button to trigger the function
submit_button = tk.Button(app, text="Submit", command=get_entry_text)
submit_button.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
