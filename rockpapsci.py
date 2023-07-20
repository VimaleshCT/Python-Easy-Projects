import random

while(True):
    user = input("enter ur choice,(rock,paper,scissor):")
    opt = ["rock", "paper", "scissor"]

    comp = random.choice(opt)

    print(f"\n you chose {user},computer chose {comp}\n")

    if (user == comp):
        print("Both selected the {user} . it is a tie!")
    elif (user == "rock"):
        if (comp == "scissor"):
            print("rock smashes scissors ^ you win!!")
        else:
            print("paper covers rock you lose")
    elif (user == "paper"):
        if (comp == "scissor"):
            print("scissors cuts paper^ you lose")
        else:
            print("paper covers rock you win!!")
    elif (user == "scissor"):
        if (comp == "paper"):
            print("scissors cuts paper^ you win!!")
        else:
            print(" rock  smashes scissor you lose")

    play_again = input("play again ? (y/n)")
    if play_again.lower() != "y":
        break