import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman")
        self.word = self.choose_word()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_attempts = 6
        
        self.word_display = tk.StringVar()
        self.word_display.set(self.display_word())

        self.word_label = tk.Label(master, textvariable=self.word_display, font=("Arial", 18))
        self.word_label.pack(pady=10)

        self.guess_label = tk.Label(master, text="Guess a letter:", font=("Arial", 12))
        self.guess_label.pack()
        
        self.guess_entry = tk.Entry(master, font=("Arial", 12))
        self.guess_entry.pack()
        
        self.guess_button = tk.Button(master, text="Guess", command=self.handle_guess, font=("Arial", 12))
        self.guess_button.pack(pady=5)
        
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_game, font=("Arial", 12))
        self.reset_button.pack(pady=5)

    def choose_word(self):
        words = ["python", "programming", "hangman", "computer", "science", "algorithm", "openai", "intelligence"]
        return random.choice(words)

    def display_word(self):
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    def handle_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)
        
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Guess", "Please enter a single alphabetical character.")
            return

        if guess in self.guessed_letters:
            messagebox.showwarning("Repeated Guess", "You've already guessed that letter!")
            return

        self.guessed_letters.append(guess)

        if guess not in self.word:
            self.incorrect_guesses += 1
            messagebox.showinfo("Incorrect Guess", f"Sorry, '{guess}' is not in the word. You have {self.max_attempts - self.incorrect_guesses} attempts left.")
        else:
            messagebox.showinfo("Correct Guess", f"Good guess! '{guess}' is in the word.")

        self.word_display.set(self.display_word())

        if "_" not in self.display_word():
            messagebox.showinfo("Congratulations!", f"You guessed the word: {self.word}")
            self.reset_game()

        if self.incorrect_guesses >= self.max_attempts:
            messagebox.showinfo("Game Over", f"Sorry, you're out of attempts. The word was: {self.word}")
            self.reset_game()

    def reset_game(self):
        self.word = self.choose_word()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.word_display.set(self.display_word())

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
