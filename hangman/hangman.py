# Setup
secret_word = "esternocleidomastoideo"
dash_word = '_' * len(secret_word)

fails = 0
max_fails = 7
success = False

# Game Loop
while not success and fails < max_fails:

    # Show the player the current state
    print ('The word is: ' + dash_word)
    print(f'You have {max_fails - fails} wrong guesses left. ')

    guess = input('Write the word or a letter: ').lower()

    # Input Handling

    # Case 1: Player guesses the whole word
    if len(guess) > 1:
        if guess == secret_word:
            success = True
            dash_word = secret_word  # Reveal the word
        else:
            print("Sorry, that's not the word.")
            fails = fails + 1

    # Case 2: Player guesses a single letter
    elif len(guess) == 1:
        found = False

        # New string
        new_dash_word = ""

        # Loop through the secret word with index (i) and letter (character)
        for i, character in enumerate(secret_word):
            if guess == character:
                new_dash_word += character # Add the real letter
                found = True
            else:
                new_dash_word += dash_word[i]

        # replace
        dash_word = new_dash_word

        if not found:
            print("Sorry, that letter isn't in the word. ")
            fails = fails + 1

        # Check if they've won by filling all the blanks
        if '_' not in dash_word:
            success = True

    # Case 3: Player didn't type anything
    else:
        print("You didn't type anything. Please try again")

# End of Game
print("-" * 20) # Separator
if success:
    print('Congratulations! You won! The word was: ' + secret_word)
else:
    print('Game over! You ran out of guesses.')
    print('The word was: ' + secret_word)
