import tkinter as tk

# Main window
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("420x620")
root.resizable(False, False)
root.configure(bg="#1e1e1e")


# Display
display = tk.Entry(
    root,
    font=("Arial", 32),
    bg="#2b2b2b",
    fg="white",
    insertbackground="white",
    justify="right",
    bd=0
)
display.pack(fill="x", padx=20, pady=(25, 20), ipady=20)


# Functions
def press(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def delete():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


def calculate():
    try:
        expression = display.get()
        expression = expression.replace("×", "*").replace("÷", "/")
        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, result)

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Button design
button_font = ("Arial", 20, "bold")

buttons = [
    ["AC", "DEL", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["00", "0", ".", "="]
]


# Create buttons
for row in buttons:

    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(expand=True, fill="both", padx=15)

    for button in row:

        if button == "AC":
            command = clear

        elif button == "DEL":
            command = delete

        elif button == "=":
            command = calculate

        else:
            command = lambda x=button: press(x)

        tk.Button(
            frame,
            text=button,
            font=button_font,
            fg="white",
            bg="#333333",
            activebackground="#555555",
            activeforeground="white",
            bd=0,
            command=command
        ).pack(
            side="left",
            expand=True,
            fill="both",
            padx=5,
            pady=5
        )


root.mainloop()