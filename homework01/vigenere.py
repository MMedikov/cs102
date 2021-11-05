def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    key = generateKey(plaintext, keyword)
    ciphertext = ""
    for i in range(len(plaintext)):
        charCode = ord(plaintext[i])
        shift = ord(key[i])
        if (charCode >= 65 and charCode <= 90) or (charCode >= 97 and charCode <= 255):
            if (plaintext[i].isupper()):
                base = 65
            else:
                base = 97

            x = ((charCode - base + shift - base) % 26) + base
            ciphertext += chr(x)
        else:
            ciphertext += chr(charCode)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    key = generateKey(ciphertext, keyword)
    plaintext = ""
    for i in range(len(ciphertext)):
        charCode = ord(ciphertext[i])
        shift = ord(key[i])
        if (charCode >= 65 and charCode <= 90) or (charCode >= 97 and charCode <= 255):
            if (ciphertext[i].isupper()):
                base = 65
            else:
                base = 97

            x = ((charCode - shift) % 26) + base
            plaintext += chr(x)
        else:
            plaintext += chr(charCode)
    return plaintext

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
