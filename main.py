def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    second = lambda tup: tup[1]
    for k, v in sorted(chars_dict.items(), key=second, reverse=True):
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")

    print("--- End report ---")

def get_chars_dict(text):
    chars = {}
    for c in text.lower():
        chars[c] = chars.get(c, 0) + 1
    return chars

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
