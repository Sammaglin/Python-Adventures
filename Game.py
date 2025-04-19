import random

def generate_guess():
    return random.randint(1, 100)

print("Welcome to the Random Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

correct_number = generate_guess()  # Generate the number once before the loop
attempts = 0
score = 0

while True:
    try:
        c_input = int(input("ENTER YOUR GUESS----> "))
        attempts += 1  # Increment attempts on every guess
        
        if c_input < correct_number:
            print("Ohoo! You guessed too low! Try again..")
        elif c_input > correct_number:
            print("Ohoo! You guessed too high! Try again..")
        else:
            score += 1  # Increment score on correct guess
            print("Congratulations! You guessed the correct number!")
            print("Your Score is", score)
            print("It took you", attempts, "attempts.")
            break  # Exit the loop after a correct guess
    except ValueError:
        print("Please enter a valid integer.")  # Handle non-integer input

    


