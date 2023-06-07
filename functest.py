def apply_case(word, case):
    match case:
        case "lower":
            cased_word = word.lower()
            return cased_word
        case "UPPER":
            cased_word = word.upper()
            return cased_word
        case "PascalCase":
            cased_word = word.capitalize()
            return cased_word
        case "Swapped":
            cased_word = word.swapcase()
            return cased_word
        case "sPoNgEbOb":
            # TODO: per-word or to the entire final one
            cased_word = []
            spongebob_list = []
            for n in word:
                spongebob_list.append(n.upper() if word.index(n) % 2 == 0 else n.lower())   # TODO: reversible
            cased_word = ''.join(spongebob_list)
            return cased_word
        case "RanDoM":
            cased_word = []
            random_list = []
            for n in word:
                rand = random.randrange(0, 10, 1)
                random_list.append(n.upper() if rand > 5 else n.lower())
            cased_word = ''.join(random_list)
            return cased_word
