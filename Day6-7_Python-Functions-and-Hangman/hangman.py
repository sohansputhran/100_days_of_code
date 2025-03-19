import random
from hangman_arts import hangman_logo, hangman_stages


with open("Day6-7_Python-Functions-and-Hangman\hangman_words.txt", "r") as f:
    word_list = f.read().split()

print(hangman_logo)
print("Welcome to Hangman!")
print("****************************************")

chosen_word = random.choice(word_list)
print(chosen_word)

display = ""
for letter in chosen_word:
    display += "_"
print(display)

lives = 6
game_over = False

while not game_over:
    print(f"****************************************{lives}/6 LIVES LEFT****************************************")
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display = display[:position] + guess + display[position + 1:]
    
    print("Word to guess:", display)

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word. You lose a life.")
        print(f"Number of life left: {lives}")
        if lives == 0:
            game_over = True
            print(hangman_stages[6 - lives])
            print(f"****************************************THE WORD WAS {chosen_word}. You lose!****************************************")
            break

    if "_" not in display:
        print("****************************************You win!****************************************")
        break
    
    print(hangman_stages[6 - lives])
    