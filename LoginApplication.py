from tkinter import *
from tkinter import messagebox

# Create Window
root = Tk()
root.title("Login Application")
root.geometry("350x250")
root.configure(bg="lightblue")

# Function to check login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

# Heading
heading = Label(root, text="Login Application",
                font=("Arial", 16, "bold"),
                bg="blue", fg="white")
heading.pack(fill=X, pady=10)

# Username
username_label = Label(root, text="Username:", bg="lightblue",
                       font=("Arial", 12))
username_label.pack(pady=5)

username_entry = Entry(root, width=25)
username_entry.pack()

# Password
password_label = Label(root, text="Password:", bg="lightblue",
                       font=("Arial", 12))
password_label.pack(pady=5)

password_entry = Entry(root, width=25, show="*")
password_entry.pack()

# Login Button
login_button = Button(root, text="Login",
                      command=login,
                      bg="green", fg="white",
                      width=12)
login_button.pack(pady=15)

# Run Window
root.mainloop()