from stats import count_words, get_book_text, count_characters, dict_to_sorted_list
import sys

def main(): 
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
    file = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    text = get_book_text(file)
    print("----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_counts = count_characters(text)
    sorted_char_counts = dict_to_sorted_list(char_counts)
    for item in sorted_char_counts:
        char = item["char"]
        count = item["count"]
        print(f"{char}: {count}")
    print("============= END ===============")

main()