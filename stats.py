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
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(items):
    return items["count"]

def dict_to_sorted_list(char_count):
    sorted_list = []
    for key in char_count:
        value = char_count[key]
        new_dict = {"char": key, "count": value}
        sorted_list.append(new_dict)
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list