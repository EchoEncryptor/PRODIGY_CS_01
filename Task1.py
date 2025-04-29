# Caesar Cipher Encryption and Decryption Program
# This script allows the user to encrypt or decrypt a message using the Caesar Cipher algorithm.

import string

def encrypt(text: str, shift: int) -> str:
    """
    Encrypts the given text using a Caesar Cipher with the specified shift.
    Maintains case and leaves non-alphabetic characters unchanged.
    """
    result = []
    for char in text:
        if char.isupper():
            # Shift uppercase characters in A-Z
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        elif char.islower():
            # Shift lowercase characters in a-z
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            # Leave non-alphabetic characters unchanged
            result.append(char)
    return ''.join(result)


def decrypt(text: str, shift: int) -> str:
    """
    Decrypts the given text by reversing the shift used in encryption.
    """
    return encrypt(text, -shift)


def main():
    print("=== Caesar Cipher ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    if choice not in ('E', 'D'):
        print("Invalid choice. Please choose 'E' for encrypt or 'D' for decrypt.")
        return

    text = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (0-25): "))
    except ValueError:
        print("Shift value must be an integer.")
        return

    shift %= 26  # Ensure shift is within 0-25

    if choice == 'E':
        result = encrypt(text, shift)
        print(f"Encrypted message: {result}")
    else:
        result = decrypt(text, shift)
        print(f"Decrypted message: {result}")


if __name__ == "__main__":
    main()
