# Find all words in a list that are typed using alternating hands on a QWERTY keyboard
from english_words import get_english_words_set
import random

web2lowerset = get_english_words_set(['web2'], alpha=True, lower=True)
wordlist = list(web2lowerset)


# TODO: Create configuration options for word selection: word length min/max, include/exclude string, ?
# TODO: Create configuration options for list: Length, ?
# TODO: Logic to concatenate strings of words with option(default?) to alternate each word's first letter (LH v RH)
# TODO: Sliding scale for semantic relation strength to previous word? (Datamuse API)


# CONFIG: LAYOUT
# TODO: Selectable/configurable keyboard layouts
lefthand = {"q", "a", "z", "w", "s", "x", "e", "d", "c", "r", "f", "v", "t", "g", "b"}
righthand = {"y", "h", "n", "u", "j", "m", "i", "k", "o", "l", "p"}

# CONFIG: CASE
case = "PascalCase"                 # TODO: configurable

def apply_case(word, case):
    match case:
        case "lower":
            cased_word = word.lower()
        case "UPPER":
            cased_word = word.upper()
        case "PascalCase":
            cased_word = word.capitalize()
        case "Swapped":
            cased_word = word.swapcase()
        case "sPoNgEbOb":
            # TODO: per-word or to the entire final one
            cased_word = []
            spongebob_list = []
            for n in word:
                spongebob_list.append(n.upper() if word.index(n) % 2 == 0 else n.lower())   # TODO: reversible
            cased_word = ''.join(spongebob_list)
        case "RanDoM":
            cased_word = []
            random_list = []
            for n in word:
                rand = random.randrange(0, 10, 1)
                random_list.append(n.upper() if rand > 5 else n.lower())
            cased_word = ''.join(random_list)
    return cased_word

# CONFIG: FINAL STRING
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
        sentence.append(apply_case(this_word, case))
        cur_sentence_length += 1
    else:
        print("What the fuck did you do??")

final_string = ''.join(sentence)

print(final_string)

# _dict_.keys()