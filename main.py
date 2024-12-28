def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_counts = get_count_by_character(text)

    print_report(book_path, word_count, letter_counts)


def get_book_text(book_path):
    with open(book_path) as book:
        return book.read()


def get_word_count(text):
    return len(text.split())


def get_count_by_character(text):
    letter_count = {}
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter.isalpha():
            if lower_letter in letter_count:
                letter_count[lower_letter] += 1
            else:
                letter_count[lower_letter] = 1

    return letter_count


def convert_to_list(dict):
    return [{"letter": k, "num": v} for k, v in dict.items()]


def sort_on(dict):
    return dict["num"]


def print_report(file_path, word_count, letter_counts):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document.")
    print("")
    letter_count_list = convert_to_list(letter_counts)
    letter_count_list.sort(key=sort_on, reverse=True)
    for letter in letter_count_list:
        print(f"The '{letter['letter']}' character was found {letter['num']} times.")
    print(f"--- End report ---")


main()
