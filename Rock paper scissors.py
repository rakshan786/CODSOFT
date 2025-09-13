import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x600")
root.config(bg="#f0f0f0")

choices = ["Rock", "Paper", "Scissors"]
history = []  # To keep track of game history

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"

def play(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    # Update labels
    user_label.config(text=f"Your Choice: {user_choice}")
    computer_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result)

    # Add to history
    round_summary = f"You: {user_choice}, Computer: {computer_choice} → {result}"
    history.append(round_summary)
    update_history()

    # Enable play again
    play_again_btn.config(state="normal")
    disable_buttons()

def update_history():
    history_text.delete("1.0", tk.END)
    for round_result in history:
        history_text.insert(tk.END, round_result + "\n")

def play_again():
    user_label.config(text="Your Choice: ")
    computer_label.config(text="Computer's Choice: ")
    result_label.config(text="")
    play_again_btn.config(state="disabled")
    enable_buttons()

def disable_buttons():
    rock_btn.config(state="disabled")
    paper_btn.config(state="disabled")
    scissors_btn.config(state="disabled")

def enable_buttons():
    rock_btn.config(state="normal")
    paper_btn.config(state="normal")
    scissors_btn.config(state="normal")

# GUI Widgets
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#f0f0f0")
title.pack(pady=10)

user_label = tk.Label(root, text="Your Choice: ", font=("Arial", 14), bg='yellow')
user_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 14), bg='grey')
computer_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="blue", bg="#f0f0f0")
result_label.pack(pady=15)

# Buttons for choices
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, font=("Arial", 12), command=lambda: play("Rock"), bg='red')
paper_btn = tk.Button(button_frame, text="Paper", width=10, font=("Arial", 12), command=lambda: play("Paper"), bg='lightgreen')
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, font=("Arial", 12), command=lambda: play("Scissors"), bg='lightpink')

rock_btn.grid(row=0, column=0, padx=10, pady=10)
paper_btn.grid(row=0, column=1, padx=10, pady=10)
scissors_btn.grid(row=0, column=2, padx=10, pady=10)

# Play again button
play_again_btn = tk.Button(root, text="Play Again", font=("Arial", 12, "bold"), bg="#add8e6",
                           command=play_again, state="disabled")
play_again_btn.pack(pady=10)

# History display
history_label = tk.Label(root, text="Game History", font=("Arial", 14, "bold"), bg="#f0f0f0")
history_label.pack(pady=5)

history_text = tk.Text(root, height=10, width=55, font=("Arial", 10), bg="#ffffff", state="normal")
history_text.pack(pady=10)

# Run the app
root.mainloop()
