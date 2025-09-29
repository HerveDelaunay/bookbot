def get_num_words(text):
    text_as_list = text.split()
    return len(text_as_list)


def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(dict):
    return dict["num"]


def get_sorted_list(char_dict):
    list = []
    for char in char_dict:
        list.append({"char": char, "num": char_dict[char]})
    list.sort(reverse=True, key=sort_on)
    return list
