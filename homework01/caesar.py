import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        code = ord(char)
        if (code >= 65 and code <= 90) or (code >= 97 and code <= 255): 
            if (char.isupper()): 
                ciphertext += chr((code + (shift - 65)) % 26 + 65) 
            else: 
                ciphertext += chr((code + (shift - 97)) % 26 + 97) 
        else: 
            ciphertext += chr(code) 
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        code = ord(char)
        if (code >= 65 and code <= 90) or (code >= 97 and code <= 255):
            if (char.isupper()):
                plaintext += chr((ord(char) - (shift + 65)) % 26 + 65)
            else:
                plaintext += chr((ord(char) - (shift + 97)) % 26 + 97) 
        else:
            plaintext += chr(code) 
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    for i in range(0,26):
        plain_text = decrypt_caesar(ciphertext, i) 
        if plain_text in dictionary:
           best_shift = i
    
    return best_shift
