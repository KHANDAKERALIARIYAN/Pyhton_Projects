import random

while True:
    your_choice = input("Do you want to roll the dice? (y/n): ").lower()
    if(your_choice=='y'):
        dice_roll1 = random.randint(1, 6)
        dice_roll2 = random.randint(1, 6)
        print(f"You rolled a ({dice_roll1},{dice_roll2})!")

    elif(your_choice=='n'):
        print("Thank you for playing!")
        break 
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
