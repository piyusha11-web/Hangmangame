import random

# List of words
words = ["apple", "banana", "orange", "computer", "python"]

# Random word
secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Hangman stages
hangman = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]

print("====== HANGMAN GAME ======")

while wrong_guesses < max_wrong:

    # Display current hangman
    print(hangman[wrong_guesses])

    # Display word
    display = ""
    word_guessed = True

    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
            word_guessed = False

    print("Word:", display)

    if word_guessed:
        print("\n🎉 Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")

# Game Over
if wrong_guesses == max_wrong:
    print(hangman[wrong_guesses])
    print("💀 Game Over!")
    print("The word was:", secret_word)