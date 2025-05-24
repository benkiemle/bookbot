import sys
from stats import count_words, count_per_character, get_sorted_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main(args):

    if (len(args) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = args[1]

    contents = get_book_text(book)
    word_count = count_words(contents)
    char_count = count_per_character(contents)
    sorted_chars = get_sorted_characters(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")

main(sys.argv)