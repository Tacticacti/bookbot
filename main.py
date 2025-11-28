from stats import count_words, get_book_text, count_characters

def main(): 
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")
    char_counts = count_characters(get_book_text("books/frankenstein.txt"))
    print(char_counts)

main()