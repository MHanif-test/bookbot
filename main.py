from stats import get_num_words, count_characters, sorted_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = sys.argv
    if len(filepath) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(filepath[1])
    num_words = get_num_words(book_text)
    count_chars = count_characters(book_text)
    list_sort_dicti = sorted_dict(count_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in list_sort_dicti:
        for key in item:
            if key.isalpha() == True:
                print(f"{key}: {item[key]}")
    print("============= END ===============")

main()