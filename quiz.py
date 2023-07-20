def check_guess(guess, ans):
    global score
    attempt = 0
    g = True

    while g and attempt < 2:
        if guess.lower() == ans.lower():
            print("correct answer !")
            score += 1
            g = False
        else:
            if attempt < 1:
                guess = input("sorry,Wrong attempt,pls try again")
                attempt += 1
    if attempt == 2:
        print("sorry, correct ans is:",ans)
    print()


score = 0
print("Guess the correct Answer:")

guess1 = input('What is the name of fastest animal?')
check_guess(guess1,"Tiger")
guess2 = input('Biggest animal on earth?')
check_guess(guess2,"Blue Whale")
guess3 = input('Which kind of bear lives in North Pole?')
check_guess(guess3, "Polar Bear")

print("your total score is:" + str(score))
