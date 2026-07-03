from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title("Getting Started with Widgets")
root.geometry("450x450")
root.configure(bg="white")

# -----------------------
# Add Image
# -----------------------
photo = PhotoImage(file="welcome.png")

image_label = Label(root, image=photo, bg="white")
image_label.pack(pady=10)

# -----------------------
# Heading
# -----------------------
heading = Label(
    root,
    text="Getting Started with Widgets",
    font=("Arial", 16, "bold"),
    bg="#072F5F",
    fg="white",
    pady=10
)
heading.pack(fill=X)

# -----------------------
# Name Input
# -----------------------
name_label = Label(
    root,
    text="Enter Your Name",
    font=("Arial", 12),
    bg="white"
)
name_label.pack(pady=10)

name_entry = Entry(root, width=30, font=("Arial", 12))
name_entry.pack()

# -----------------------
# Text Box
# -----------------------
text_box = Text(root, width=40, height=5, font=("Arial", 11))
text_box.pack(pady=15)

# -----------------------
# Button Function
# -----------------------
def display():

    name = name_entry.get()

    text_box.delete(1.0, END)

    if name == "":
        text_box.insert(END, "Please enter your name.")
    else:
        text_box.insert(END, f"Hello {name}!\n")
        text_box.insert(END, "Welcome to the Application.\n")
        text_box.insert(END, f"Today's Date: {date.today()}")

# -----------------------
# Button
# -----------------------
button = Button(
    root,
    text="Begin",
    command=display,
    bg="#1261A0",
    fg="white",
    font=("Arial", 12)
)
button.pack()

# Run Application
root.mainloop()