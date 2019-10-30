import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        option = input("Did you mean %s instead Enter Y if yes and N if no: " % get_close_matches(word, data.keys())[0])
        if option == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif option == "N":
            return "This word does not exist, please double check the word"
        else:
            return "we didn't understand your entry"
    else:
        return "This word does not exist, please double check the word"

word = input("Enter a word: ") 

definition = translate(word)

if type(definition) == list:
    for item in definition:
        print(item)
else:
    print(definition)