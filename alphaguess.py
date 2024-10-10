from sowpods import d
from smalldict import smalld
import random as rand

def compare_alpha(word1, word2):
    '''1 for word one first, 0 for word2 first, and 2 for same word'''
    
    lets = 'abcdefghijklmnopqrstuvwxyz'
    letd = {lets[i]: i for i in range(26)}
    min_length = min([len(word1), len(word2)])

    for i in range(min_length):
        if i == min_length - 1:
            if lets[letd[word1[i]]] == lets[letd[word2[i]]]:
                if len(word1) < len(word2):
                    return 1
                elif len(word1) > len(word2):
                    return 0
                else:
                    return 2
        if lets[letd[word1[i]]] == lets[letd[word2[i]]]:
            continue
        if lets[letd[word1[i]]] < lets[letd[word2[i]]]:
            return 1
        else:
            return 0

def run_alpha_guess():

    word = smalld[rand.randint(0, len(smalld) - 1)]
    win = False
    c = 0
    word_after = None
    word_before = None

    while not win:
        print('\n')
        if word_after:
            print(f"The word comes before {word_after}")
        if word_before:
            print(f"The word comes after {word_before}")

        guess = input('Type a valid english word: ').lower()
        c += 1

        if guess not in d:
            print('Not a valid word')
            c -= 1
            continue

        if guess == word:
            win = True
            print(f"You win. It took you {c} words.")
            break

        if compare_alpha(guess, word):
            print(f"The word comes after {guess}")
            if not word_before:
                word_before = guess
            else:
                if not compare_alpha(guess, word_before):
                    word_before = guess
        else:
            print(f"The word comes before {guess}")
            if not word_after:
                word_after = guess
            else:
                if compare_alpha(guess, word_after):
                    word_after = guess

run_alpha_guess()