"""A program that take English words and return its definition in English"""

# importing the json library to load the dictionary file
import json
# importing get_close_matches from difflib to check for close matches when the word doesn't exist
from difflib import get_close_matches

# Loading the dictionary file
data = json.load(open("data.json"))

# Getting the word from the user to translate
word = input("Enter a word: ")


# Finding the word in the dictionary file and returning its definition
def search(word):
    """A function to check if the user's input is in the dictionary file.
    If yes, return the definition of the word. If no, check if there're any close match and return the definition of the closest match.
    Or return a "The word doesn't exist. Please double check it." message"""

    # making the program letter case insensitive
    word = word.lower()

    # check if the user's input is in the dictionary file
    if word in data:
        # return the definition of the word
        return data[word]

    # if the word is not in the dictionary file, check if there're any close matches
    elif len(get_close_matches(word, data.keys())) > 0: #incase any close matches found
        #ask the user if the closest match is what was meant
        find_match = input(f"Do you mean {get_close_matches(word, data.keys())[0]}? if yes enter Y if no enter N: ")
        #if the answer is yes

        if find_match.upper() == "Y":
            #return the definition of the closest match
            return data[get_close_matches(word, data.keys())[0]]

        #if the answer is no
        elif find_match.upper() == "N":
            #return a message to the user
            return "The word doesn't exist. Please double check it."

        #if the answer is not a y or n, return a message to the user
        return "We didn't understand your entry."

    # if the word is not in the dictionary file and there're no close matches, return a message to the user
    return word + " doesn't exist"


# Calling the function and printing out the returned value
print(search(word))
