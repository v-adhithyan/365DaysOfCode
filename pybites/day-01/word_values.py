import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    f = open(DICTIONARY, "r")
    return [lines.strip() for lines in f.readlines()]


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    return sum(map(lambda letter: LETTER_SCORES[letter.upper()], word))


def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    max_val = 0
    result = ""
    for word in words:
        current_value = calc_word_value(word)
        if current_value > max_val:
            max_val = current_value
            result = word
    return result
