"""Test for Secret Garden."""


from secret_garden import Decoder, SecretGarden

file = 'pr08_example_data.txt'
key = 'Fat Chocobo'


def test_decode():
    """Test Decode."""
    d = Decoder(file, key)

    assert len(d.decode()) == 7
    assert d.read_code_from_file() == ['KS0uNyktBgZBT08=', 'LTU3KS0wBgZKQVNKQU9PQVNK', 'KTA3KTIGBkFKU0FKQUpPQUpKQUFP', 'LjcpLwYGQUpTU0FKU0pPT1NTT09PUw==', 'LSw3MAYG', 'LDcpLSwGBk9BQVNTT1NPQUFBU0FBQUFB', 'LjcpLgYGU09TQU9KQU9PTw==']
    assert d.decode_from_base64('MDsyCgpOTlNXV0U=') == '0;2\n\nNNSWWE'
    assert d.calculate_cipher_step() == 1016
    assert d.decode()[0] == '-12;-1\n\nESS'
    assert d.decode()[1] == '19;-14\n\nNEWNESSEWN'


def test_garden():
    """Testing Secret Garden."""
    sg = SecretGarden(file, key)

    assert sg.find_secret_locations()[0] == (-11, -3)
    assert sg.find_secret_locations()[1] == (20, -13)

    assert sg.decode_messages()[1] == '19;-14\n\nNEWNESSEWN'
