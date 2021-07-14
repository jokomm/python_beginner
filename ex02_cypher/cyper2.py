"""Encode and decode text using Rail-fence Cipher."""


def encode(message: str, key: int) -> str:
    """
    Encode text using Rail-fence Cipher.

    Replace all spaces with '_'.

    :param message: Text to be encoded.
    :param key: Encryption key.
    :return: Decoded string.
    """
    message = message.replace(' ', '_')
    code = ""
    if key == 1:
        return message
    table = zik_zak(message, key)
    i, m = 0, 0
    while i < key:
        if table[i][m] != '.':
            code += message[m]
        m += 1
        if m == len(message):
            m = 0
            i += 1
    return code


def decode(message: str, key: int) -> str:
    """
    Decode text knowing it was encoded using Rail-fence Cipher.

    '_' have to be replaced with spaces.

    :param message: Text to be decoded.
    :param key: Decryption key.
    :return: Decoded string.
    """
    if key == 1:
        return message.replace('_', ' ')
    table = zik_zak(message, key)
    index = 0
    for zig in range(key):
        for zag in range(len(message)):
            if table[zig][zag] == '*':
                table[zig][zag] = message[index]
                index += 1
    down_move = True
    zig = 0
    decode_cipher = ""
    for zag in range(len(message)):
        decode_cipher += table[zig][zag]
        if zig == 0:
            zig += 1
            down_move = True
        elif zig == key - 1:
            zig -= 1
            down_move = False
        elif down_move:
            zig += 1
        elif not down_move:
            zig -= 1
    return decode_cipher.replace('_', ' ')


def make_table(message, key):
    """Make a table for future functions."""
    table = []
    for _ in range(key):
        row = []
        for _ in range(len(message)):
            row.append('.')
        table.append(row)
    return table


def zik_zak(message, key):
    """Application of zigzag movement."""
    down_move = True
    zig = 0
    table = make_table(message, key)
    for zag in range(len(message)):
        table[zig][zag] = '*'
        if zig == 0:
            zig += 1
            down_move = True
        elif zig == key - 1:
            zig -= 1
            down_move = False
        elif down_move:
            zig += 1
        elif not down_move:
            zig -= 1
    return table


if __name__ == '__main__':
    print(encode("Mind on vaja krüpteerida", 3))  # => M_v_prido_aaküteiannjred
    print(encode("Mind on", 3))  # => M_idonn
    print(encode("hello", 1))  # => hello
    print(encode("hello", 8))  # => hello
    print(encode("kaks pead", 1))  # => kaks_pead

    print(decode("kaks_pead", 1))  # => kaks pead
    print(decode("M_idonn", 3))  # => Mind on
    print(decode("M_v_prido_aaküteiannjred", 3))  # => Mind on vaja krüpteerida