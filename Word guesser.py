secret_word = "GALAXY"
guess = ""
prompt = "A massive system of stars, gas, and dust bound together by gravity."
attempts_count = 0
attempts_limit = 3
out_of_limit = False
# Variables
print("Welcome to the word guesser game".upper())
print("I will give a hint and you have to guess the word in 3 attempts".upper())
print(prompt)
while secret_word != guess and not out_of_limit:
    if attempts_count < attempts_limit:
        guess = input("Enter your guess---> ").upper()
        attempts_count += 1
        print("Attempt number ",attempts_count)
    else:
        out_of_limit = True
        print("You are out of limits")
if secret_word == guess:
    print("You Win".upper())
