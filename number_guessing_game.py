#Importing Libraries
import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        self.master.title("Number Guessing Game")
        
        # Generate a random number between 1 and 100
        self.random_number = random.randint(1, 100)
        
        # Create and place the label that provides instructions to the player
        self.label = tk.Label(master, text="I have selected a number between 1 and 100. Can you guess it?")
        self.label.pack()
        
        # Create and place an entry widget for user input
        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()
        
        # Create and place a button that the player clicks to submit their guess
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()
        
        # Create and place a label to display the result (too high, too low, or correct)
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
    
    def check_guess(self):
        # Get the user's guess from the entry widget
        guess = self.guess_entry.get()
        
        # Check if the input is a valid number
        if not guess.isdigit():
            # Show an error message if the input is not a valid number
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return
        
        # Convert the guess from string to integer
        guess = int(guess)
        
        # Compare the guess with the randomly generated number
        if guess < self.random_number:
            # Inform the user that the guess is too low
            self.result_label.config(text="Too low! Try again.")
        elif guess > self.random_number:
            # Inform the user that the guess is too high
            self.result_label.config(text="Too high! Try again.")
        else:
            # Inform the user that they have guessed correctly
            self.result_label.config(text="Congratulations! You guessed the number.")
            # Show a message box to congratulate the user
            messagebox.showinfo("Success", "Congratulations! You guessed the number.")
            # Reset the game for another round
            self.reset_game()
    
    def reset_game(self):
        # Generate a new random number for the next round
        self.random_number = random.randint(1, 100)
        # Clear the entry widget for the next guess
        self.guess_entry.delete(0, tk.END)
        # Reset the result label
        self.result_label.config(text="")

def main():
    # Create the main application window
    root = tk.Tk()
    # Create an instance of the game
    game = NumberGuessingGame(root)
    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
