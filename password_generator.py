import tkinter as tk
from tkinter import messagebox
import string
import random


# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x500")
root.resizable(False, False)
root.configure(bg="#1e1e1e")


# Title
title = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 26, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=(35, 10))


# Subtitle
subtitle = tk.Label(
    root,
    text="Create a strong random password",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="#aaaaaa"
)
subtitle.pack(pady=(0, 25))


# Length Label
length_label = tk.Label(
    root,
    text="Password Length",
    font=("Arial", 13, "bold"),
    bg="#1e1e1e",
    fg="white"
)
length_label.pack()


# Length Entry
length_entry = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center",
    bg="#2b2b2b",
    fg="white",
    insertbackground="white",
    bd=0
)
length_entry.pack(pady=10, ipadx=10, ipady=8)


# Password Display
password_entry = tk.Entry(
    root,
    font=("Arial", 18),
    justify="center",
    bg="#2b2b2b",
    fg="white",
    insertbackground="white",
    bd=0
)
password_entry.pack(pady=20, padx=40, fill="x", ipady=10)


# Generate Password
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning(
                "Invalid Length",
                "Password length should be at least 4."
            )
            return

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = ''.join(
            random.choice(characters)
            for _ in range(length)
        )

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number."
        )


# Copy Password
def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )
    else:
        messagebox.showwarning(
            "No Password",
            "Generate a password first."
        )


# Clear
def clear_all():
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# Generate Button
generate_button = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 14, "bold"),
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    bd=0,
    command=generate_password
)
generate_button.pack(pady=10, ipadx=20, ipady=8)


# Buttons Frame
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)


# Copy Button
copy_button = tk.Button(
    button_frame,
    text="Copy",
    font=("Arial", 12, "bold"),
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    bd=0,
    command=copy_password
)
copy_button.pack(side="left", padx=8, ipadx=20, ipady=6)


# Clear Button
clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    bd=0,
    command=clear_all
)
clear_button.pack(side="left", padx=8, ipadx=20, ipady=6)


# Run Application
root.mainloop()