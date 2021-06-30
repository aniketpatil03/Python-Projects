import random

# Generating random word from list
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print("psst, the chosen random word", chosen_word)

# Generating as many blanks as the word
display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

game_over = False

while not game_over:  # Condition for while loop to keep going
    # Taking input guess from user
    guess = input("Enter your guess: ").lower()

    # Replacing the blank value with guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        game_over = True        # Condition which is required to end while loop or goes infinite
        print("Game Over, you won")
