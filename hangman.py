from tkinter import *
from tkinter import messagebox, simpledialog
import random
import re

#====================

def pick_rndm_word(*args):
    # Load .txt file with list of words
    with open("list_of_words.txt", "r") as f:
        words = f.readlines()
    # Generate random integer to choose one word from the given file
    nr_word = random.randrange(0, len(words))
    # Pick the random word
    word = words[nr_word]
    # Return the word without the line break at the end
    return word[:-1]

def initialize_game(*args):
    # Call function to generate a random word
    word = pick_rndm_word()
    # Create placeholder text to display
    guess_word = "-" * len(word)
    word_label.config(text=guess_word)
    return word, guess_word

def hangman(*args):
    # Call function that picks random word and displays the placeholder text
    word, guess_word = initialize_game()
    # The actual game starts here
    while word != guess_word:
        # Ask for string input (should be a character only) and put the input in lower case
        guess_char = simpledialog.askstring("Input", "Guess a character:", parent=root).lower()
        # Check if only one character was entered
        if len(guess_char) != 1:
            messagebox.showerror("Error", "Please enter only single characters!")
        # Check if the entered character is valid
        elif ord(guess_char) < 97 or ord(guess_char) > 122:
            messagebox.showerror("Error", "Please enter only valid characters (a-z)!")
        else:
            # Find all occurences of the guessed character in the word
            char_index = [c.start() for c in re.finditer(guess_char, word)]
            # Check if the character occurs in the word
            if len(char_index) == 0:
                messagebox.showinfo("Try again!", "The word doesn't contain that character! Try again!")
            else:
                # Replace the dashes with the guessed character
                for i in char_index:
                    guess_word = guess_word[:i] + guess_char + guess_word[i+1:]
                # Update the displayed text
                word_label.config(text=guess_word)

#====================

# Create a window
root = Tk()
# Set the window title
root.title("Hangman - The Game")
# Set window size
root.geometry("512x384")

#====================

# Create text labels (start, exit)
start_label = Label(root, text="Start the game:")
exit_label = Label(root, text="Close the window:")
word_label = Label(root, font=("times", 20))

# Create buttons (start, exit)
start_button = Button(root, text="Start", command=hangman)
exit_button = Button(root, text="Exit", command=root.destroy)

#====================

# Add components to the window
# Text labels
start_label.place(x = 106, y = 10, width=150, height=30)
exit_label.place(x = 106, y = 50, width=150, height=30)
word_label.place(x = 0, y = 130, width=512, height=60)

# Buttons
start_button.place(x = 256, y = 10, width=150, height=30)
exit_button.place(x = 256, y = 50, width=150, height=30)

# Wait for user input
root.mainloop()