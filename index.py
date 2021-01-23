import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[word]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(
            f"Did you mean {get_close_matches(w, data.keys())[0]}? Enter Y if yes or N if no: ")
        if yn == "Y" or yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        else:
            print("Sorry that word does not exist.")
    else:
        print("The word doesn't exist, please double check it.")


word = input("Enter Word: ")

print(translate(word))
