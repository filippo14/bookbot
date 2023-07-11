def main():
    rel_book_path = "books/frankenstein.txt"
    book_text = get_book(rel_book_path)
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)

    print("--- Begin report of books/frankenstein.txt --- \n\n")
    print(f"{num_words} words found in the document \n")

    sorted_chars = sort_characters(num_chars)

    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

    print("\n\n--- End report ---")


def sort_characters(chars):
    sorted_chars = sorted(chars.items(), key=lambda x: x[0])
    return sorted_chars


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    chars = dict()
    for c in text:
        if c.isalpha():
            char_lower = c.lower()
            if char_lower in chars:
                chars[char_lower] += 1
            else:
                chars[char_lower] = 1
    
    return chars


def get_book(path):
    with open(path) as f:
         return f.read()


main()