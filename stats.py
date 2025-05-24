def count_words(text):
    words = text.split()
    return len(words)

def count_per_character(text):
    text = text.lower()
    characters = {}

    for c in text:
        if characters.get(c) == None:
            characters[c] = 0

        characters[c] += 1

    return characters

def get_sorted_characters(character_counts: dict):
    result = []

    for c in character_counts:
        result.append({ "char": c, "num": character_counts[c]})

    return sorted(result, key=lambda s: s["char"])