import random
import os

def clear_screen():
    """Clears the console screen. Tries to use 'cls' or 'clear',
    falls back to printing newlines if that fails."""
    try:
        # For Windows
        if os.name == 'nt':
            _ = os.system('cls')
        # For macOS and Linux
        else:
            _ = os.system('clear')
    except OSError:
        # Fallback for environments where 'cls' or 'clear' are not available
        # or where the TERM environment variable is not set.
        print('\n' * 100)

def get_random_word():
    """Selects a random word and its category from a predefined list."""
    word_list = {
        "Fruits": ["apple", "banana", "mango", "strawberry", "orange", "grape", "pineapple"],
        "Animals": ["tiger", "elephant", "lion", "monkey", "giraffe", "zebra", "penguin"],
        "Countries": ["india", "canada", "australia", "japan", "brazil", "egypt", "spain"],
        "Programming Languages": ["python", "javascript", "java", "ruby", "swift", "golang"]
    }

    category = random.choice(list(word_list.keys()))
    word = random.choice(word_list[category])
    return word.upper(), category.upper()

def display_hangman(tries):
    """Displays the hangman ASCII art corresponding to the number of incorrect tries."""
    stages = [  # Final state: head, torso, both arms, both legs
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \
           -
        """,
        # Head, torso, both arms, one leg
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
           -
        """,
        # Head, torso, both arms
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
           -
        """,
        # Head, torso, one arm
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
           -
        """,
        # Head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # Head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # Initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

def play_game():
    """Main function to play the Hangman game."""
    word, category = get_random_word()
    word_completion = "_" * len(word)
    guessed_letters = []
    guessed_words = []
    tries = 6
    playing = True

    print("Let's play Hangman!")
    input("Press Enter to start...")

    while playing and tries > 0:
        clear_screen()
        print(f"Topic: {category}")
        print(display_hangman(tries))
        print(f"Word: {' '.join(word_completion)}\n")  # Added join for better spacing
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}\n")
        print("-------------------------")

        guess = input("Guess a letter or the full word: ").upper()

        # --- Input Validation ---
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter '{guess}'.")
            elif guess not in word:
                print(f"'{guess}' is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! '{guess}' is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word '{guess}'.")
            elif guess != word:
                print(f"'{guess}' is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                word_completion = word  # Correct guess

        else:
            print("Invalid input. Please enter a single letter or a word of the correct length.")

        # --- Check for win condition ---
        if "_" not in word_completion:
            playing = False

        if tries > 0 and playing:
            input("\nPress Enter to continue...")

    # --- Game Over ---
    clear_screen()
    if "_" not in word_completion:
        print("Congratulations, you guessed the word! You win!")
        print(f"The word was: {word}")
    else:
        print(f"Sorry, you ran out of tries. The word was '{word}'.")
        print(display_hangman(0))  # Show the full hangman

def main():
    """Main menu for the game."""
    while True:
        play_game()
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

