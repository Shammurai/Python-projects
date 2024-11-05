import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I have picked a number between 1 and 100.")
    print("Try to guess it!")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_the_number()