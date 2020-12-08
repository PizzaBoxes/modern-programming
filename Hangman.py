import random

# Desc.

# 1. Pick secret word from list
#   Initializing variable and making a random variable to select from list
#   Save the secret word into a variable

# words = open('words.txt')
#word_list = words.read() .split('\n')

#random.shuffle(word_list)
#word = word_list[0]

words = ['epitome', 'suspicious', 'reasonable', 'accompaniment', 'crisp', 'apple', 'orange', 'banana', 'grapes', 'avenue', 'tree', 'trilogy', 'book', 'look', 'vocabulary', 'necessary', 'goodbye', 'heartbreak', 'wardrobe', 'detergent', 'snake', 'dog', 'cat', 'pig', 'bird', 'parrot', 'carrot', 'potato', 'backpack', 'boat']
random.shuffle(words)
word = words[0]

# Letters left to guess; the blank lines

# Counting characters


# Make a system that will say the word they guessed is wrong or right


# Setting the secret word

secret_word = word
secret_word_list = list(secret_word)
secret_word_set = set()

for character in secret_word:
    secret_word_set.add(character)
#    print(character + " in Secret Word Set")
letters_displayed = "-" * len(secret_word)

guessed_list = []

number_tries = 5

winning_condition = False

correct_guesses = set()

ask_answer = raw_input

body = "|------\n|\n|\n|\n|\n|\n|\n|_____"
body1 = "|-----|\n|\n|\n|\n|\n|\n|\n|_____"
body2 = "|-----|\n|     O\n|\n|\n|\n|\n|\n|_____"
body3 = "|-----|\n|     O\n|     | \n|     |\n|\n|\n|\n|_____"
body4 = "|-----|\n|     O\n|    /| \n|   / |\n|\n|\n|\n|_____"
body5 = "|-----|\n|     O\n|    /|\ \n|   / | \ \n|\n|\n|\n|_____"
body6 = "|-----|\n|     O\n|    /|\ \n|   / | \ \n|    /\n|   /\n|\n|_____"
body7 = "|-----|\n|     O\n|    /|\ \n|   / | \ \n|    / \ \n|   /   \ \n|\n|_____"

# 2. Ask user for their guess letter
print"Secret Word : ", letters_displayed
print "Let's play Hangman!"
print(body)
print "All the words in this game are random, and picked from a list."
print "Guess only ONE letter at a time."
print "You only have 5 guesses.\nTry to avoid guessing the same letter twice; it will take a life if it's an incorrect guess."
print "What's your first guess? "

while (number_tries > 0, winning_condition == False):
#   Ask the user to guess a letter, get input, and store their guess in a variable

    guess = raw_input()
    #ask = "Do you want to play again? (yes or no)"

# 3. Guess letter and secret word
# if number_tries is 0:
# Check if the letter guessed is in the word

    if guess in secret_word:
#   and tell user it's correct
        print "You guessed a correct letter."
        correct_guesses.add(guess)

# Update dashes
        index = 0
        letters_displayed_list = list(letters_displayed)
        while index < len(letters_displayed_list):
            if guess == secret_word_list[index]:
                letters_displayed_list[index] = guess
            index = index + 1
        letters_displayed = "".join(letters_displayed_list)
    print "Secret Word: ", letters_displayed


            #       and display it
            #           with a variable that keeps track of the user's guesses

            # 4. If it's wrong, then tell them it's wrong
            #   then add wrong letter to list of ALL letters

    if guess not in secret_word:
        print "You guessed an incorrect letter."
        guessed_list.append(guess)

        print "Wrong letters guessed: ", guessed_list

        number_tries = number_tries - 1
        if number_tries is 5:
            print body1
        if number_tries is 4:
            print body2
        if number_tries is 3:
            print body3
        if number_tries is 2:
            print body4
        if number_tries is 1:
            print body5
        if number_tries is 0:
            print body6
        if number_tries is -1:
            print body7

            # Words guessed bank
            # 5. Game over after 6 tries or word is guessed
    if (correct_guesses == secret_word_set):
        winning_condition = True
        print "Congratulations, you won!"
        print "* ,  # '\n'   /_\   ,\n*  \ O / . '\n ,  \|/   *\n  '  |  ,''. \n    / \  *  . :\n .,/   \ ,,.  '"
        print "The word was", secret_word + "!"
        #print ask
        break

    if number_tries is -1:
        print "You used all your tries! You lost!"
        print "The word was", secret_word + "!"
        #print ask
        break

    if guess == secret_word:
        winning_condition = True
        print "Congratulations, you won!"
        print "* ,  # '\n'   /_\   ,\n*  \ O / . '\n ,  \|/   *\n  '  |  ,''. \n    / \  *  . :\n .,/   \ ,,.  '"
        print "The word was", secret_word + "!"
        break
        #print ask

    if guess == " " or guess == "":
        print "Please guess a letter."

    if guess == "":
        print "(It's not actually correct, but I won't take any guesses off for that.)"


if number_tries is -1 or winning_condition is True or correct_guesses == secret_word_set:
    print "Would you like to play again?"

    if ask_answer == 'yes' or ask_answer == 'Yes':
        print "Okay, let's reset the game!"

    elif ask_answer == 'no' or ask_answer == 'No':
        print "Okay, that was fun!"
        exit()
    else:
        print "Please pick yes or no. "
