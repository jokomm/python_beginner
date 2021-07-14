"""Shifting letters."""


def encode(message: str, key: int) -> str:
    """
    Encode a message using a Caesar cipher.

    Presume the message is already lowercase.
    For each letter of the message, shift it forward in the alphabet by key amount.
    If the character isn't a letter, keep it the same.

    E.g. key = 3 a->d, b->e
    encode('i like turtles', 6) -> 'o roqk zaxzrky'
    encode('example', 1) -> 'fybnqmf'
    encode('the quick brown fox jumps over the lazy dog.', 7) -> 'aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.'

    :param message: message to be encoded
    :param key: key for encoding
    :return: encoded message
    """
    encoded = ""

    for letter in message:
        if letter.isalpha():
            shifted_letter = ord(letter) - ord("a")   # ord() converts a character to its numeric representation in Unicode.
            shift = (shifted_letter + key) % 26  # shift it according to key
            new_unicode = shift + ord("a")  # find new unicode
            new_letter = chr(new_unicode)   # convert back to letter
            encoded = encoded + new_letter
        else:
            encoded += letter    # if not alpha leave it

    return encoded


if __name__ == '__main__':
    print(encode("i like turtles", 6))  # -> o roqk zaxzrky
    print(encode("o roqk zaxzrky", 20))  # -> i like turtles
    print(encode("example", 1))  # -> fybnqmf
    print(encode("don't change", 0))  # -> don't change
    print(encode('the quick brown fox jumps over the lazy dog.', 7))  # -> aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.

