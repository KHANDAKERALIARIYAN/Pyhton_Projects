import random

number_to_Guess= random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))

        if (guess < number_to_Guess ):
            print("Too low . Try again!")
        elif(guess > number_to_Guess):
            print("Too high. Try again!")
        else:
            print("Congratulations! You guessed the number!")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
