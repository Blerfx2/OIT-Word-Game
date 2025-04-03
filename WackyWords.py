import requests
import random

def main():
    # Starts the game
    print ("Welcome to Wacky Words!")
    while True:
        difficulty = input(f"Please choose your difficulty (length of word)\n easy (1), medium (2), hard (3): ")
        if difficulty not in ["1","2","3"]: 
            print("Please type 1, 2, or 3 to choose a difficulty")
        else:
            break
    # Calculates difficulty
    difficulty = int(difficulty) - 1
    difficulties = ["easy", "medium", "hard",]
    difficulty_num = 4 + difficulty * 2
    # Fetches word from API
    word = requests.get(f"https://random-word-api.vercel.app/api?words=1&length={difficulty_num}").json()[0]
    print(f"You chose the {difficulties[difficulty]} difficulty. Let's begin!\n\n")

    # Instructions
    print(f"""Here's how you play!
    You will be guessing letters to figure out a word.
    If you guess a letter in the word, it will be revealed in the position that it is in the word
    When guessing, please make sure to type only one lowercase letter.
    Be careful! You can only get 7 guesses wrong before you lose!
    If you accidentally guess more than one letter or an uppercase letter, you will not lose a guess.
    You may alternatively type 'help' to get a letter revealed to you. You may only use this once.
    Good luck!\n\n""")
    
    guesses = 0
    guessed_letters = []
    has_helped = False
    while guesses < 7:
        word_so_far = ""
        for letter in word:
            if letter in guessed_letters:
                word_so_far += letter
            else:
                word_so_far += "_"
        
        if word == word_so_far:
            print(f"Congratulations! You guessed the word!\nYour word was {word}")
            break

        print(f"The word so far: {word_so_far}\nMistakes remaining: {7-guesses}")
        guess = input("What's your Guess? ")

        if len(guess) == 1 and guess.islower():
            if guess in guessed_letters:
                print(f"You've already guessed this letter\n")

            elif guess in word:
                print(f"Good job! {guess} is in the word!\n")

            else:
                print(f"Uh oh! {guess} was not in the word. Try again!\n")
                guesses += 1
            guessed_letters.append(guess)

        # Optional hint system
        elif guess == "help":
            if has_helped is False:
                while True:
                    help_letter = random.choice(word)
                    if help_letter not in guessed_letters:
                        print(f"Your hint is {help_letter}!\n")
                        guessed_letters.append(help_letter)
                        has_helped = True
                        break
            else:
                print("You can only be helped once!\n")

        else:
            print(f"Invalid input. Please type a single, lowercase letter\n")

    if guesses == 7:
        print(f"I'm so sorry, you did not guess the word.\nYour word was {word}\n")

    again = input("If you would like to play again, type y, otherwise type whatever you want: ")
    if again == "y":
        main()
    else:
        print("Goodbye. Hope to see you again!")

                
        




if __name__ == "__main__":
    main()