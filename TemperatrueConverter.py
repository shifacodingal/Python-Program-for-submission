from tkinter import *

# Function to convert temperature
def convert():
    temp = float(entry.get())
    unit = option.get()

    if unit == "Celsius to Fahrenheit":
        result = (temp * 9/5) + 32
        output.config(text=f"Temperature: {result:.2f} °F")

    elif unit == "Fahrenheit to Celsius":
        result = (temp - 32) * 5/9
        output.config(text=f"Temperature: {result:.2f} °C")


# Create Window
root = Tk()
root.title("Temperature Converter")
root.geometry("350x300")
root.configure(bg="lightblue")

# Heading
heading = Label(root,
                text="Temperature Converter",
                font=("Arial", 16, "bold"),
                bg="blue",
                fg="white")
heading.pack(fill=X, pady=10)

# Temperature Entry
Label(root,
      text="Enter Temperature:",
      bg="lightblue",
      font=("Arial", 12)).pack(pady=5)

entry = Entry(root, font=("Arial", 12))
entry.pack()

# Dropdown Menu
option = StringVar()
option.set("Celsius to Fahrenheit")

menu = OptionMenu(root, option,
                  "Celsius to Fahrenheit",
                  "Fahrenheit to Celsius")
menu.pack(pady=10)

# Convert Button
Button(root,
       text="Convert",
       command=convert,
       bg="green",
       fg="white",
       font=("Arial", 11)).pack()

# Result Label
output = Label(root,
               text="Temperature:",
               bg="lightblue",
               font=("Arial", 13))
output.pack(pady=20)

# Run Application
root.mainloop()