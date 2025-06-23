def get_num_words(text):
    return len(text.split())

def count_chars(content):
    characters = {}
    content = content.lower()
    for l in content :
        if l not in characters:
            characters[l] = 0;
        characters[l] += 1
    return characters

def sort_on(items):
    return items["num"]

def count_chars_sorted(chars):
    characters = []
    for char in chars:
        characters.append({"char": char, "num": chars[char]})
    characters.sort(reverse=True, key=sort_on)
    return characters