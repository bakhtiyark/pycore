"""Implement the keyword encoding and decoding for the Latin alphabet. The keyword cipher uses a keyword to rearrange the letters in the alphabet. You should add the provided keyword at the beginning of the alphabet. A keyword is used as the key, which determines the letter matchings of the cipher alphabet to the plain alphabet. The repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C, etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.

Encryption:

The keyword is "Crypto"

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
Example:

>>> cipher = Cipher("crypto")
>>> cipher.encode("Hello world")
"Btggj vjmgp"

>>> cipher.decode("Fjedhc dn atidsn")
"Kojima is genius"""


class Cipher:
    def __init__(self, keyword):
        self.keyword = keyword.lower()
        self.cipher_alphabet = self.generate_cipher_alphabet()

    def generate_cipher_alphabet(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        unique_letters = sorted(set(self.keyword), key=self.keyword.index)
        cipher_alphabet = self.keyword + \
            "".join(letter for letter in alphabet if letter not in unique_letters)
        return cipher_alphabet

    def encode(self, text):
        encoded_text = ""

        for char in text:
            if char.isalpha():
                lower_char = char.lower()
                index = ord(lower_char) - ord('a')
                if char.isupper():
                    encoded_text += self.cipher_alphabet[index].upper()
                else:
                    encoded_text += self.cipher_alphabet[index]
            else:
                encoded_text += char

        return encoded_text

    def decode(self, encrypted_text):
        decoded_text = ""

        for char in encrypted_text:
            if char.isalpha():
                lower_char = char.lower()
                index = self.cipher_alphabet.index(lower_char)
                if char.isupper():
                    decoded_text += chr(index + ord('A'))
                else:
                    decoded_text += chr(index + ord('a'))
            else:
                decoded_text += char

        return decoded_text

cipher = Cipher("crypto")

encoded_text = cipher.encode("Hello world")
print(encoded_text)  # Output: "Btggj vjmgp"

decoded_text = cipher.decode("Fjedhc dn atidsn")
print(decoded_text)  # Output: "Kojima is genius"
