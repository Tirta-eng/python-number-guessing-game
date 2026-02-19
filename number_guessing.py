import random

def play_game():
    secret_number = random.randint(1, 20)
    max_attempts = 5
    attempts = 0

    print("=== NUMBER GUESSING GAME ===")
    print("Guess the number between 1 and 20.")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            score = (max_attempts - attempts + 1) * 20
            print("🎉 Correct!")
            print(f"You guessed it in {attempts} attempts.")
            print(f"Your score: {score}")
            return

        print(f"Remaining attempts: {max_attempts - attempts}")

    print("\nGame Over.")
    print(f"The secret number was {secret_number}")
    print("Your score: 0")

if __name__ == "__main__":
    play_game()
