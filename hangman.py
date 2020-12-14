import random

# Reading in the words
f = open("words.txt", "r")
ls_words = f.readlines()
f.close()

# Picking a word
LENGTH = len(ls_words)
random_word_index = random.randint(0, LENGTH)
WORD = list(ls_words[random_word_index].strip("\n").lower())
print("The word has", len(WORD), "letters", "_" * len(WORD))


def game():
    count = 0
    player_guesses = ["_"] * len(WORD)
    available_letters = ["a ", "b ", "c ", "d ",
                         "e ", "f ", "g ", "h ",
                         "i ", "j ", "k ", "l ",
                         "m ", "n ", "o ", "p ",
                         "q ", "r ", "s ", "t ",
                         "u ", "v ", "w ", "x ", "y ", "z"]
    while player_guesses != WORD and count != 6:
        print("Available letters: " + " ".join(available_letters))
        letter = input(str("Enter your guess: "))
        while not (isinstance(letter, str) and letter.isalpha()):
            letter = input(str("Enter again: "))
        if letter in WORD:
            for i in range(len(WORD)):
                if WORD[i] == letter:
                    player_guesses[i] = letter
            print("your guess so far: " + " ".join(player_guesses))
            if player_guesses == WORD:
                print("You guessed", "".join(WORD), "with ", 6 - count,
                      " to spare!")
        else:
            count += 1
            print("Oops " + letter + " is not in the word!")
            print("lives left:", 6 - count)
            print("your guess so far: " + " ".join(player_guesses))
        if count == 6:
            print("the word was", "".join(WORD))
            print("better luck next time!")
        available_letters.remove(letter + " ")


if __name__ == "__main__":
    game()
