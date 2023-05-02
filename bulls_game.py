import random

def generate_secret_number():
    """Generate a 4-digit secret number with no repeated digits."""
    digits = list(random.sample(range(10), 4))
    random.shuffle(digits)
    return digits

def get_guess():
    """Prompt the user to enter a guess and validate the input."""
    while True:
        guess = input("Enter a 4-digit number with no repeated digits: ")
        if not guess.isdigit() or len(guess) != 4 or len(set(guess)) != 4:
            print("Invalid input. Please enter a 4-digit number with no repeated digits.")
        else:
            return [int(digit) for digit in guess]

def evaluate_guess(secret, guess):
    """Evaluate the guess and return the number of bulls and cows."""
    bulls = sum(secret[i] == guess[i] for i in range(4))
    cows = sum(secret.count(guess[i]) for i in range(4)) - bulls
    return bulls, cows

def play_game():
    """Play the Bulls and Cows game."""
    secret = generate_secret_number()
    guesses = 0
    while True:
        guesses += 1
        guess = get_guess()
        bulls, cows = evaluate_guess(secret, guess)
        print(f"{bulls} bulls, {cows} cows")
        if bulls == 4:
            print(f"Congratulations, you guessed the secret number in {guesses} guesses!")
            break

play_game()
