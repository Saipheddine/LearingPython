# this is the hangman game 
import random

# flag to check if the game is over or not
game_not_over = True

# letters' list to create random words
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                'x', 'y', 'z']

# creates a random word with a random length
def randomWordCreator():
    res = ""
    word_len = 6
    while word_len > 0:
        rand_index = random.randint(0, word_len - 1)
        res += letters[rand_index]
        word_len -= 1
    return res

# udpates the word if a char is guessed right!
def updateWord(word_to_update, char, original_word):
    char_occurances = original_word.count(char)
    if (char_occurances > 0):
        tmp_list = list(word_to_update)
        for i in range(0, len(original_word)):
            if (original_word[i] == char):
                tmp_list[i] = char
                word_to_update = "".join(str(elem) for elem in tmp_list)
    return word_to_update

print("game has just started!")

word_to_guess = randomWordCreator()
len_of_word_to_guess = len(word_to_guess)

# output the word as dashes before starting to guess it
dashes = ""
for i in word_to_guess:
    dashes += "-"

times_to_guess = 6

print("Guess the word!")


updated_word = dashes

while (game_not_over):
    char = input("Give a character\t")
    updated_word = updateWord(updated_word, char, word_to_guess)
    print(updated_word)
    times_to_guess -= 1
    if (updated_word == word_to_guess):
        print("You won!")
        game_not_over = False
    elif times_to_guess == 0:
        if updated_word == word_to_guess:
            print("You Won!")
        else:
            print("You lost!")    
        game_not_over = False   


