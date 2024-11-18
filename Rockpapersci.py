import tkinter as tk
from tkinter import messagebox
import random


class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("400x400")
        self.root.configure(bg="#282c34")  

        # Score Variables
        self.user_score = 0
        self.computer_score = 0

        # GUI Components
        self.instruction_label = tk.Label(
            root, text="Choose Rock, Paper, or Scissors:", 
            font=("Arial", 14, "bold"), fg="#ffffff", bg="#282c34"
        )
        self.instruction_label.pack(pady=20)

        # Buttons
        self.rock_button = tk.Button(
            root, text="Rock", width=10, font=("Arial", 12, "bold"), bg="#6c757d", fg="#ffffff",
            activebackground="#adb5bd", activeforeground="#000000",
            command=lambda: self.play_round("Rock")
        )
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(
            root, text="Paper", width=10, font=("Arial", 12, "bold"), bg="#007bff", fg="#ffffff",
            activebackground="#5a9bd8", activeforeground="#000000",
            command=lambda: self.play_round("Paper")
        )
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(
            root, text="Scissors", width=10, font=("Arial", 12, "bold"), bg="#28a745", fg="#ffffff",
            activebackground="#72d076", activeforeground="#000000",
            command=lambda: self.play_round("Scissors")
        )
        self.scissors_button.pack(pady=5)

        # Result and Score Labels
        self.result_label = tk.Label(
            root, text="", font=("Arial", 12, "bold"), fg="#f8f9fa", bg="#282c34"
        )
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(
            root, text="Score: You - 0 | Computer - 0", font=("Arial", 12, "bold"), fg="#f8f9fa", bg="#282c34"
        )
        self.score_label.pack(pady=10)

        # Play Again Button
        self.play_again_button = tk.Button(
            root, text="Play Again", font=("Arial", 12, "bold"), bg="#ff4757", fg="#ffffff",
            activebackground="#ff6b81", activeforeground="#000000",
            command=self.reset_game, state=tk.DISABLED
        )
        self.play_again_button.pack(pady=10)

    def play_round(self, user_choice):
        """Play a round of Rock-Paper-Scissors."""
        options = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(options)

        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            result = "You Win!"
            self.user_score += 1
        else:
            result = "You Lose!"
            self.computer_score += 1

        # Update result and score
        self.result_label.config(
            text=f"You chose {user_choice}, Computer chose {computer_choice}.\n{result}",
            fg="#f8f9fa"
        )
        self.score_label.config(
            text=f"Score: You - {self.user_score} | Computer - {self.computer_score}"
        )
        self.play_again_button.config(state=tk.NORMAL)

        # Disable buttons after a round
        self.rock_button.config(state=tk.DISABLED)
        self.paper_button.config(state=tk.DISABLED)
        self.scissors_button.config(state=tk.DISABLED)

    def reset_game(self):
        """Reset the game for another round."""
        self.result_label.config(text="")
        self.play_again_button.config(state=tk.DISABLED)
        self.rock_button.config(state=tk.NORMAL)
        self.paper_button.config(state=tk.NORMAL)
        self.scissors_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
