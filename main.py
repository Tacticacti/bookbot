from stats import count_words, get_book_text, count_characters, dict_to_sorted_list

def main(): 
    print("============ BOOKBOT ============")
    file = "books/frankenstein.txt"
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