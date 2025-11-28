def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(text):  
    words = text.split()
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    char_count = {}
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count