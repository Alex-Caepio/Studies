text = 'asdRTJKasd'
dupl_dict = {}


def duplicate_text(text):
    for letter in text:
        if letter in dupl_dict:
            dupl_dict[letter] += 1
        else:
            dupl_dict[letter] = 1

    return dupl_dict


print(duplicate_text(text))
