import random

# List of words
words = ["python", "laptop", "coding", "robot", "apple"]

# Select random word
secret_word = random.choice(words)

# Create hidden word display
display = ["_"] * len(secret_word)

# Store guessed letters
guessed_letters = []

# Number of lives
lives = 6

print("=" * 40)
print("WELCOME TO HANGMAN GAME")
print("=" * 40)

while lives > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    print("Lives Remaining:", lives)

    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess

        print("Correct Guess!")

    else:
        lives -= 1
        print("Wrong Guess!")

# Result
if "_" not in display:
    print("\nCongratulations!")
    print("You guessed the word:", secret_word)

else:
    print("\nGame Over!")
    print("The word was:", secret_word)