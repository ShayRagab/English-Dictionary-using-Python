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

    if word in data: # check if the user's input is in the dictionary file
        return data[word] # return the definition of the word

    elif word.upper() in data: # check for names such as USA and NATO
        return data[word.upper()] #returns the definition

    elif word.title() in data: # check for cities/states names that start with a capital letter
        return data[word.title()] #returns the definition

    elif len(get_close_matches(word, data.keys())) > 0: # check if there're any close matches
        #ask the user if the closest match is what was meant
        find_match = input(f"Do you mean {get_close_matches(word, data.keys())[0]}? if yes enter Y if no enter N: ")

        if find_match.upper() == "Y": #if the answer is yes
            return data[get_close_matches(word, data.keys())[0]] #return the definition of the closest match

        elif find_match.upper() == "N": #if the answer is no
            return "The word doesn't exist. Please double check it." #return a message to the user

        return "We didn't understand your entry." #if the answer is not a y or n, return a message to the user

    return word + " doesn't exist" # if the word is not in the dictionary file and no close matches found

# setting the output of the search() function into a variable
output = search(word)

# Prints every item of the search() function output into a seperate line
if type(output) == list: # check if the output is a list
    for item in output: # for every item in the output list print the item
        print(item)
else: # if the output is not a list, print the output
    print(output)
