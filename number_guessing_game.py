"""
Number Guessing Game — GUI Version (Tkinter)
Works on Windows (Python 3.14+)
"""

import tkinter as tk
import random


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        self.secret = 0
        self.remaining = 0
        self.upper = 0

        self.create_difficulty_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_difficulty_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="🎮 Number Guessing Game",
                 font=("Arial", 16, "bold")).pack(pady=15)

        tk.Label(self.root, text="Choose Difficulty",
                 font=("Arial", 12)).pack(pady=10)

        tk.Button(self.root, text="Easy (1–50, 10 tries)",
                  command=lambda: self.start_game(50, 10),
                  width=25).pack(pady=5)

        tk.Button(self.root, text="Medium (1–100, 7 tries)",
                  command=lambda: self.start_game(100, 7),
                  width=25).pack(pady=5)

        tk.Button(self.root, text="Hard (1–200, 5 tries)",
                  command=lambda: self.start_game(200, 5),
                  width=25).pack(pady=5)

    def start_game(self, upper, attempts):
        self.upper = upper
        self.remaining = attempts
        self.secret = random.randint(1, upper)

        self.clear_screen()

        tk.Label(self.root, text=f"Guess a number (1–{upper})",
                 font=("Arial", 12)).pack(pady=10)

        self.info_label = tk.Label(self.root,
                                   text=f"Attempts left: {self.remaining}",
                                   font=("Arial", 10))
        self.info_label.pack()

        self.entry = tk.Entry(self.root, font=("Arial", 12), justify="center")
        self.entry.pack(pady=10)

        tk.Button(self.root, text="Submit Guess",
                  command=self.check_guess).pack(pady=5)

        self.message_label = tk.Label(self.root, text="", font=("Arial", 10))
        self.message_label.pack(pady=10)

        tk.Button(self.root, text="Change Difficulty",
                  command=self.create_difficulty_screen).pack(pady=5)

    def check_guess(self):
        guess = self.entry.get()

        if not guess.isdigit():
            self.message_label.config(text="❌ Enter numbers only!")
            return

        guess = int(guess)

        if guess < 1 or guess > self.upper:
            self.message_label.config(
                text=f"❌ Enter number between 1 and {self.upper}")
            return

        self.remaining -= 1
        self.info_label.config(text=f"Attempts left: {self.remaining}")

        if guess == self.secret:
            self.message_label.config(
                text="🎉 Correct! You won!")
            self.end_game()
        elif self.remaining == 0:
            self.message_label.config(
                text=f"💀 Game Over! Number was {self.secret}")
            self.end_game()
        elif guess < self.secret:
            self.message_label.config(text="⬆ Too Low! Go higher")
        else:
            self.message_label.config(text="⬇ Too High! Go lower")

        self.entry.delete(0, tk.END)

    def end_game(self):
        tk.Button(self.root, text="Play Again",
                  command=self.create_difficulty_screen).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    NumberGuessingGame(root)
    root.mainloop()