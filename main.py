from stats import get_book_text, word_count, get_chars_dict, dict_sort
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_dict = get_chars_dict(text)
    dict_sorts = dict_sort(chars_dict)
    print_report(book_path, num_words, dict_sorts)

def print_report(book_path, num_words, dict_sorts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in dict_sorts:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")



main()