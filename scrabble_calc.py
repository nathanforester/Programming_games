import sys

while True:

    word = input("please enter a word of four letters or more to calculate score (you may press 'x' anytime to exit): ")

    dictionary_scrab = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                        "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                        "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                        "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                        "x": 8, "z": 10}


    def scrabble_calc(word):
        output = 'word not long enough'
        if len(word) >= 4:
            return sum(dictionary_scrab[letter] for letter in word)
        elif len(word) < 4 and word != 'x':
            return output



    print(scrabble_calc(word))

    if word == 'x':
        break

