from stats import get_num_words, get_chars_dict, get_sorted_list
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    num_words = get_num_words(get_book_text(filepath))
    chars_dict = get_chars_dict(get_book_text(filepath))
    sorted_chars = get_sorted_list(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print(f"----------- Word Count ----------\nFound {num_words} total words.")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}\n")
    print("============= END ===============")


main()
