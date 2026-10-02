import tkinter as tk
import random


# Main Window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#1e1e1e")


# Score
user_score = 0
computer_score = 0


# Title
title = tk.Label(
    root,
    text="Rock • Paper • Scissors",
    font=("Arial", 26, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=(35, 10))


subtitle = tk.Label(
    root,
    text="Choose your move",
    font=("Arial", 13),
    bg="#1e1e1e",
    fg="#aaaaaa"
)
subtitle.pack(pady=(0, 30))


# Result
result_label = tk.Label(
    root,
    text="Make your choice!",
    font=("Arial", 22, "bold"),
    bg="#1e1e1e",
    fg="white"
)
result_label.pack(pady=20)


# Choices
choice_label = tk.Label(
    root,
    text="You: -     Computer: -",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="#cccccc"
)
choice_label.pack(pady=10)


# Score
score_label = tk.Label(
    root,
    text="You  0   :   0  Computer",
    font=("Arial", 16, "bold"),
    bg="#1e1e1e",
    fg="white"
)
score_label.pack(pady=20)


# Game Logic
def play(user_choice):

    global user_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "Draw!"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1

    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)

    choice_label.config(
        text=f"You: {user_choice}     Computer: {computer_choice}"
    )

    score_label.config(
        text=f"You  {user_score}   :   {computer_score}  Computer"
    )


# Button Style
button_font = ("Arial", 15, "bold")


# Rock Button
rock_button = tk.Button(
    root,
    text="🪨  Rock",
    font=button_font,
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    bd=0,
    command=lambda: play("Rock")
)
rock_button.pack(pady=8, ipadx=45, ipady=10)


# Paper Button
paper_button = tk.Button(
    root,
    text="📄  Paper",
    font=button_font,
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    bd=0,
    command=lambda: play("Paper")
)
paper_button.pack(pady=8, ipadx=45, ipady=10)


# Scissors Button
scissors_button = tk.Button(
    root,
    text="✂  Scissors",
    font=button_font,
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    bd=0,
    command=lambda: play("Scissors")
)
scissors_button.pack(pady=8, ipadx=45, ipady=10)


# Reset Game
def reset_game():

    global user_score, computer_score

    user_score = 0
    computer_score = 0

    result_label.config(text="Make your choice!")
    choice_label.config(text="You: -     Computer: -")
    score_label.config(text="You  0   :   0  Computer")


reset_button = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 12, "bold"),
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    bd=0,
    command=reset_game
)
reset_button.pack(pady=25, ipadx=25, ipady=7)


root.mainloop()