def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(text):  
    words = text.split()
    return len(words)

def main(): 
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")

main()