# Find all words in a list that are typed using alternating hands on a QWERTY keyboard
from english_words import get_english_words_set
web2lowerset = get_english_words_set(['web2'], alpha=True, lower=True)
wordlist = list(web2lowerset)

# TODO: lefthand, righthand values to sets or dicts
# TODO: Selectable/configurable keyboard layouts
lefthand = set("q", "a", "z", "w", "s", "x", "e", "d", "c", "r", "f", "v", "t", "g", "b")
righthand = set("y", "h", "n", "u", "j", "m", "i", "k", "o", "l", "p")

final_length = 5                    # TODO: configurable
sentence = []                       # final string of words
cur_sentence_length = 0
i = 0

while cur_sentence_length < final_length:
    i += 1
    this_word = wordlist[i]
    letters = list(this_word)
    starting_hand = None
    other_hand = None
    letter_range = range(0,len(this_word))
    odds = set()
    evens = set()

    if letters[0].lower() in lefthand:
        starting_hand = lefthand
        other_hand = righthand
    elif letters[0].lower() in righthand:
        starting_hand = righthand
        other_hand = lefthand
    else:
        print("Please supply only letters.")

    for letter_index in letter_range:
        if letter_index %2 == 0:
            evens.add(this_word[letter_index])
        else:
            odds.add(this_word[letter_index])

    all_evens = all(x in starting_hand for x in evens)
    all_odds = all(y in other_hand for y in odds)

    if not all_evens or not all_odds:
        # print("{} is NOT a matching word!".format(this_word))
        pass
    elif all_evens and all_odds:
        sentence.append(this_word)
        cur_sentence_length += 1
    else:
        print("What the fuck did you do??")

print(sentence)
# TODO: concatenate together correcthorse style
# ''.join(listString)

# TODO: Create configuration options for word selection: word length min/max, include/exclude string, ?
# TODO: Create configuration options for list: Length, ?
# TODO: Logic to concatenate strings of words with option(default?) to alternate each word's first letter (LH v RH)
# TODO: Logic for various cases: lower, upper, random, alternating every X, pascal, ...
# TODO: Sliding scale for semantic relation strength to previous word? (Datamuse API)

# _dict_.keys()