# Find all words in a list that are typed using alternating hands on a QWERTY keyboard

import requests

words = ["aaron", "Adam", "haughty", "Jeezy", "ambient", "skeptic"]

lefthand = ["q", "a", "z", "w", "s", "x", "e", "d", "c", "r", "f", "v", "t", "g", "b"]
righthand = ["t", "g", "b", "y", "h", "n", "u", "j", "m", "i", "k", "o", "l", "p"]

matching_words = []

# {word}
url = "https://wordsapiv1.p.rapidapi.com/words/"
querystring = {"letterPattern":"[a-z|A-Z]{6,8}","limit":"20"}
headers = {
	"X-RapidAPI-Key": "ad33b108dcmsh3723a6bc9c1280fp11440ajsn440004b087de",
	"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)
print(response.json())
print(type(response))
print()




# TODO: Use the API to pull in a list of dictionary words
# TODO: Create configuration options for word selection: word length min/max, include/exclude string, ?
# TODO: Create configuration options for list: Length, ?




""" for letter_index in letters:
    if letter_index %2 == 0:
        if this_word[letter_index] not in starting hand:
            return false
"""




def alternate_hands_check(word, starting_hand, other_hand):
    this_word = word
    letter_range = range(0,len(word))
    odds = []
    evens = []

    for letter_index in letter_range:
        if letter_index % 2 != 0:
            odds.append(this_word[letter_index])

        elif letter_index % 2 == 0:
            evens.append(this_word[letter_index])


    all_evens = all(x in starting_hand for x in evens)
    all_odds = all(y in other_hand for y in odds)

    if not all_evens or not all_odds:
        # print("{} is NOT a matching word!".format(this_word))
        pass

    elif all_evens and all_odds:
        matching_words.append(this_word)

    else:
        print("What the fuck did you do??")

for word in words:
    global letters
    letters = list(word)
    starting_hand = None
    other_hand = None

    if letters[0].lower() in lefthand:
        starting_hand = lefthand
        other_hand = righthand

    elif letters[0].lower() in righthand:
        starting_hand = righthand
        other_hand = lefthand

    else:
        print("Please supply only letters.")

    alternate_hands_check(word, starting_hand, other_hand)

print(matching_words)















""" 

reversedString = ''.join(listString)


 """