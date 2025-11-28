from stats import count_words, get_book_text

def main(): 
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")

main()