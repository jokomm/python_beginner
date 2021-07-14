"""Encode and decode Caesar cipher."""


def encode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz") -> str:
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    if len(alphabet) == 0:
        return message
    if shift == 0:
        return message
    shift = shift_len(shift, alphabet)
    coded = str()
    alphabet2 = str.upper(alphabet)
    for char in message:
        if char.isupper() is True:
            coded = upper_char(coded, char, shift, alphabet2)
        if char not in alphabet and char not in alphabet2:
            coded += char
        else:
            coded = normal_char(char, coded, alphabet, shift)

    return coded
    pass


def decode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz") -> str:
    """
    Decode the given message already encoded with the caesar cipher principle.

    :param message: The string to be decoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Decoded string.
    """
    decoded = encode(message, -shift, alphabet)

    return decoded

    pass


def shift_len(shift, alphabet="abcdefghijklmnopqrstuvwxyz"):
    """
    Make shift readable for the program.

    Write Functions for shift.
    """
    if shift > len(alphabet):
        shift = shift % len(alphabet)
    if shift < -len(alphabet):
        shift = abs(shift) % len(alphabet)
        shift = -shift

    return shift


def normal_char(char, coded, alphabet, shift):
    """
    Function to use cesare cipher on if letters are lowercase and standard ascii.

    :param char:
    :param coded:
    :param alphabet:
    :param shift:
    :return:
    """
    for i in range(len(alphabet)):
        if char == alphabet[i]:
            if i + shift > len(alphabet):
                var2 = alphabet[i + shift - len(alphabet)]
                coded += var2
            elif i + shift < len(alphabet):
                var = alphabet[i + shift]
                coded += var
            else:
                var5 = alphabet[i]
                coded += var5
    return coded


def upper_char(coded, char, shift, alphabet2):
    """
    Function if there is uppercase character in message.

    Use this function if there is an uppercase character in message.
    """
    for l in range(len(alphabet2)):
        if char == alphabet2[l]:
            if l + shift > len(alphabet2):
                var3 = alphabet2[l + shift - len(alphabet2)]
                coded += var3
            elif l + shift < len(alphabet2):
                var1 = alphabet2[l + shift]
                coded += var1
            else:
                var4 = alphabet2[l]
                coded += var4
    return coded


if __name__ == "__main__":
    # simple tests
    print(encode("abcdefgHIjKLMNopQRStUVWxyZ", -261))  # ifmmp
    print(decode("abcdefgHIjKLMNopQRStUVWxyZ", -260))  # hello
