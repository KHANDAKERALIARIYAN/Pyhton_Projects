import random

your_Dictionary = {
    "r": -1,
    "p": 0,
    "s": 1 
}

reverse_Dictionary = {
    -1: "Rock",
    0: "Paper",
    1: "Scissors"
}

while True:
    your_choices = input("Enter your choice (r/p/s) or 'q' to quit: ").lower()
    if your_choices == 'q':
        print("Game exited.")
        break
    if your_choices not in your_Dictionary:
        print("Invalid choice! Please enter r, p, or s.")
        continue

    computer_choices = random.choice([-1, 0, 1])
    your_choice_val = your_Dictionary[your_choices]

    print(f"You chose: {reverse_Dictionary[your_choice_val]}")
    print(f"Computer chose: {reverse_Dictionary[computer_choices]}")

    if computer_choices == your_choice_val:
        print("It's a DRAW ! ")
    else:
        if computer_choices == -1 and your_choice_val == 1:
            print("You Lose !")
        elif computer_choices == -1 and your_choice_val == 0:
            print("You Win !")
        elif computer_choices == 1 and your_choice_val == -1:
            print("You Win !")
        elif computer_choices == 1 and your_choice_val == 0:
            print("You Lose !")
        elif computer_choices == 0 and your_choice_val == -1:
            print("You Lose !")
        elif computer_choices == 0 and your_choice_val == 1:
            print("You Win !")
        else:
            print("Something went wrong !")

