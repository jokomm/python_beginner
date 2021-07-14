"""Booksortation."""


def booksortation(books: list) -> dict:
    """
    Given a list of books (strings). Your task is to categorize and sort them.

    There are five books categories: spell books, history books, relics books, potion books and other books.

    If a book doesn't belong to any named categories, it goes to 'other books' category.

    However, if one book belongs to multiple categories, they should appear in only one
    (starting from up, whichever occurs first).

    :param books: given books as a list, list contains of strings
    :return: categorised and sorted books as a dict, where keys are categories and values are
    list of books that match this category. Lists should be sorted alphabetically.
    """
    categorised_books = {}

    for book in books:
        if is_spell_book(book):
            add_book_to_category(book, "spell books", categorised_books)
        elif is_history_book(book):
            add_book_to_category(book, "history books", categorised_books)
        elif is_relics_book(book):
            add_book_to_category(book, "relics books", categorised_books)
        elif is_potion_book(book):
            add_book_to_category(book, "potion books", categorised_books)
        else:
            add_book_to_category(book, "other books", categorised_books)

    for key in categorised_books:
        categorised_books[key] = sorted(categorised_books[key])

    return categorised_books




def add_book_to_category(book: str, category: str, categorised_books: dict) -> dict:
    """
    Add books to the corresponding categories.

    :param book: the book given
    :param category: the category a book belongs to
    :param categorised_books: dictonary of categorised books
    :return: list of categorised books
    """
    if category not in categorised_books:
        categorised_books[category] = [book]
    else:
        categorised_books[category].append(book)
    return categorised_books


def is_spell_book(book: str) -> bool:
    """
    Book is a spell book if its title starts with '*' (a star, without quotes) and ends with '*' (a star, no quotes).

    However, if the starting and ending star is the same star, it is not a spell book.

    For example: '*The Horrible Spells*' is a spell book.

    :param book: given book as a string
    :return: True if given book is a spell book, False otherwise
    """
    if book.startswith("*") and book.endswith("*") and len(book) >= 2:
        return True
    else:
        return False


def is_history_book(book: str) -> bool:
    """
    Book is a history book if its title matches the pattern where each new word does not start with a lowercase letter.

    Word is considered anything after a whitespace.

    For example: 'The Mighty King' and 'The Age Of The Wonderbolts' are both history books.
    Then again, 'the Ugly Duckling' isn't a history books because the word 'the' doesn't start with a capital letter.

    :param book: given book as a string
    :return: True if given book is a history book, False otherwise
    """
    uppercase = []
    lowercase = []

    for word in book.split():
        if not word[0].islower():
            uppercase.append(word)
        else:
            lowercase.append(word)
    if len(lowercase) == 0:
        return True
    else:
        return False


def is_relics_book(book: str) -> bool:
    """
    Book is a relics book if its title matches the uppercase-lowercase-uppercase-lowercase... pattern.

    It can start from both upper- and lowercase letters.
    PS! Pay attention to whitespaces.

    For example: 'ThE StAfF' and 'rAiNiNg dUmPlInGs' are both relics books.
    However 'ThE sTaFf' and 'rAiNiNg DuMpLiNgS' are not relics books.

    :param book: given book as a string
    :return: True if given book is a relics book, False otherwise
    """
    special_characters = "!@#$%^&*()-+"
    book_1 = book[::2]
    book_2 = book[1::2]
    if any(c in special_characters for c in book):
        return True
    elif book_1.isupper() and not book_1.islower() and book_2.islower() and not book_2.isupper():
        return True
    elif book_1.islower() and not book_1.isupper() and book_2.isupper() and not book_2.islower():
        return True
    elif book.isalpha() and not book_1.islower() and not book_2.isupper():
        return True
    else:
        return False


def is_potion_book(book: str) -> bool:
    """
    Book is a potion book if its title contains the same amount of vowels and consonants or the amount differs by one.

    However, it may contain as many symbols as it likes.

    The vowels are a, e, i, o, u.
    The consonants are b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, x, z, w, y.

    For example: 'The Banana Juice' is a potion book (7 vowels, 7 consonants)
    and so is 'The tomato potion' (7 vowels, 8 consonants -> differ by 1).
    However, 'The Green Liquid' isn't a potion book (6 vowels, 8 consonants -> differ by 2).

    :param book: given book as a string
    :return: True if given book is a potion book, False otherwise
    """
    vowel = set("aeiouAEIOU")
    consonant = set("bcdfghjklmnpqrstvxzwyBCDFGHJKLMNPQRSTVXZWY")
    vowel_count = 0
    consonant_count = 0
    for alphabet in book:
        if alphabet in vowel:
            vowel_count = vowel_count + 1

    for alphabet in book:
        if alphabet in consonant:
            consonant_count = consonant_count + 1

    if abs(vowel_count - consonant_count) <= 1:
        return True
    else:
        return False


if __name__ == '__main__':
    # All True.
    print(is_spell_book('*kana*'))
    print(is_history_book('This Is A History Book'))
    print(is_potion_book('The Banana Juice'))
    print(is_history_book('The Mighty King'))
    print(is_relics_book('ThE StAfF'))
    print(is_relics_book('rAiNiNg dUmPlInGs'))
    print(is_relics_book('419(!/)/(!#='))
    print(is_history_book(""))
    print(is_history_book("I FiT ThReE"))
    print(is_relics_book('aB'))
    # False.
    print(is_history_book('the Ugly Duckling'))
    print(is_relics_book('ThE sTaFf'))
    print(is_relics_book('rAiNiNg DuMpLiNgS'))
    print(is_potion_book('The Green Liquid'))
    print(is_history_book("i Am Not A History book"))
    print(is_history_book("Almost ok"))
    print(is_history_book('aB'))


