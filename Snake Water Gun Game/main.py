import random 

choices_Dictionary = {
    "snake": -1,
    "water": 0,
    "gun": 1
}

reverse_Dictionary = {
    -1: "Snake",
    0: "Water",
    1: "Gun"
}

while True:
    your_Choice = input("Enter your choice (Snake, Water, Gun) or 'q' to quit: ").lower()
    if your_Choice == 'q':
        print("Game exited.")
        break
    if your_Choice not in choices_Dictionary:
        print("Invalid choice! Please enter Snake, Water, or Gun.")
        continue

    computer = random.choice([-1, 0, 1])
    you = choices_Dictionary[your_Choice]

    print(f"You chose: {reverse_Dictionary[you]}")
    print(f"Computer chose: {reverse_Dictionary[computer]}")

    if computer == you:
        print("It's a Draw !")
    else:
        if computer == -1 and you == 1:
            print("You Win !")
        elif computer == -1 and you == 0:
            print("You Lose !")
        elif computer == 1 and you == -1:
            print("You Lose !")
        elif computer == 1 and you == 0:
            print("You Win !")
        elif computer == 0 and you == -1:
            print("You Win !")
        elif computer == 0 and you == 1:
            print("You Lose !")
        else:
            print("Something went wrong !")

