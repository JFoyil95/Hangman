from random_words import RandomWords

r = RandomWords()
replay = True
word_list = ["bunny", "puppies", "tree"]
while replay:
    word_to_guess = r.random_word()
    used_letters = []
    template = ["_"] * len(word_to_guess)
    print("~WELCOME TO HANGMAN!~")
    count = 0
    print("     _____")
    print("     |   |")
    print("         |")
    print("         |")
    print("         |")
    print("_________|___\n")
    while count < 6:
        print(template)
        print("\nUsed letters:", used_letters)
        print("\nGuess a letter, or, if you would like to guess the word, type 'Solve'.")
        guess = input().lower()
        if guess == "solve":
            guess = input("What is the word:   ").lower()
            if guess == word_to_guess:
                print("-" * 40)
                print("Correct! You win!")
                while True:
                    answer = input("\nWould you like to play again? Y/N   ").lower()
                    if answer == "y":
                        break
                    elif answer == "n":
                        print("Good Game!")
                        replay = False
                        break
                    else:
                        print("I don't understand.")
                break
            elif guess != word_to_guess:
                print("-" * 40)
                print("Sorry, that is incorrect...")
                count += 1
        elif guess != "solve":
            if len(guess) != 1:
                print("-" * 40)
                print("Please only guess one letter.")
            else:
                if guess in used_letters:
                    print("-" * 40)
                    print("You already guessed that letter!")
                elif guess not in used_letters:
                    if guess in word_to_guess:
                        print("-" * 40)
                        print("Correct!")
                        k = 0
                        for i in word_to_guess:
                            if i == guess:
                                template[k] = i
                            k += 1
                        used_letters.append(guess)
                    elif guess not in word_to_guess:
                        print("-" * 40)
                        print("Sorry, that is incorrect...")
                        used_letters.append(guess)
                        count += 1
        if "_" not in template:
            print("-" * 40)
            print(template)
            print("You guessed the word correctly!\nYou win!")
            while True:
                answer = input("\nWould you like to play again? Y/N   ").lower()
                if answer == "y":
                    break
                elif answer == "n":
                    print("Good Game!")
                    replay = False
                    break
                else:
                    print("I don't understand.")
            break
        if count == 0:
            print("     _____")
            print("     |   |")
            print("         |")
            print("         |")
            print("         |")
            print("_________|___\n")
        elif count == 1:
            print("     _____")
            print("     |   |")
            print("     O   |")
            print("         |")
            print("         |")
            print("_________|___\n")
        elif count == 2:
            print("     _____")
            print("     |   |")
            print("     O   |")
            print("     |   |")
            print("         |")
            print("_________|___\n")
        elif count == 3:
            print("     _____")
            print("     |   |")
            print("     O   |")
            print("     |-  |")
            print("         |")
            print("_________|___\n")
        elif count == 4:
            print("     _____")
            print("     |   |")
            print("     O   |")
            print("    -|-  |")
            print("         |")
            print("_________|___\n")
        elif count == 5:
            print("     _____")
            print("     |   |")
            print("     O   |")
            print("    -|-  |")
            print("      \  |")
            print("_________|___\n")
        elif count == 6:
            print("     _____")
            print("     |   |")
            print("     O   |")
            print("    -|-  |")
            print("    / \  |")
            print("_________|___\n")
            print("\nSorry, you lose...")
            print("\nThe word was", word_to_guess + ".")
            while True:
                answer = input("\nWould you like to play again? Y/N   ").lower()
                if answer == "y":
                    break
                elif answer == "n":
                    print("Good Game!")
                    replay = False
                    break
                else:
                    print("I don't understand.")