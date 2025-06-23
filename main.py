import sys
from stats import get_num_words
from stats import count_chars
from stats import count_chars_sorted

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
        

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")

    print("----------- Word Count ----------")
    content = get_book_text(file)
    num_words = get_num_words(content)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    chars = count_chars(content)
    chars = count_chars_sorted(chars)
    for char in chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()