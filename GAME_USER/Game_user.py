
import random

def number_guessing_game():
    print("🔢 Welcome! Think of a number between 1 and 100, and I'll try to guess it.")

    minimum = 1
    maximum = 100

    while True:
        computer_guess = random.randint(minimum, maximum)
        print(f"🤔 Hmm... Is it {computer_guess}?")

        response = input("Type 'too low', 'too high', or 'yes' if I got it right: ").lower().strip()

        if response == 'too low':
            minimum = computer_guess + 1
        elif response == 'too high':
            maximum = computer_guess - 1
        elif response == 'yes':
            print(f"🎉 Woohoo! I guessed it: {computer_guess} was your number!")
            break
        else:
            print("⚠️ Please reply with 'too low', 'too high', or 'yes'.")

number_guessing_game()
