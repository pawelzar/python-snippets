def decrypt_vigenere(message, key):
    """
    Decrypts message using the Vigenère cipher.

    :param message: encrypted message
    :param key:
    :return: decrypted message
    """
    message_numerical = [ord(x)-97 for x in message]
    key_numerical = [ord(x)-97 for x in key]
    return ''.join(' ' if a == -65 else chr(97 + (a-b) % 26)
                   for a, b in zip(message_numerical, key_numerical))
