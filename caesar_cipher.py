"""
Project 2: Basic Encryption & Decryption
DecodeLabs - Cyber Security Internship

Goal: Implement a simple encryption and decryption technique
using the Caesar Cipher (a classic substitution cipher).

Author: <your name here>
"""


def encrypt(plaintext: str, shift: int) -> str:
    """
    Encrypts the given plaintext using a Caesar Cipher shift.

    Formula (IPO Model -> Process step):
        E_n(x) = (x + n) % 26

    Handles:
        - Uppercase letters
        - Lowercase letters
        - Spaces, numbers, punctuation (left untouched)
    """
    result = ""

    for char in plaintext:
        if char.isupper():
            # A = 65 in ASCII
            shifted = (ord(char) - 65 + shift) % 26 + 65
            result += chr(shifted)
        elif char.islower():
            # a = 97 in ASCII
            shifted = (ord(char) - 97 + shift) % 26 + 97
            result += chr(shifted)
        else:
            # Non-alphabet characters (spaces, numbers, punctuation)
            # are NOT encrypted - added as-is (edge case handling)
            result += char

    return result


def decrypt(ciphertext: str, shift: int) -> str:
    """
    Decrypts the given ciphertext using a Caesar Cipher shift.

    Formula (Reverse Engineering):
        D_n(x) = (x - n) % 26

    Symmetric Encryption: the same key (shift) locks and unlocks.
    """
    # Decryption is just encryption with the negative shift
    return encrypt(ciphertext, -shift)


def main():
    print("=" * 50)
    print(" DecodeLabs - Caesar Cipher (Encrypt & Decrypt)")
    print("=" * 50)

    # ---- INPUT ----
    user_text = input("\nEnter the text you want to encrypt: ")

    while True:
        try:
            shift_key = int(input("Enter the shift key (e.g., 3): "))
            break
        except ValueError:
            print("Please enter a valid whole number for the shift key.")

    # ---- PROCESS ----
    encrypted_text = encrypt(user_text, shift_key)
    decrypted_text = decrypt(encrypted_text, shift_key)

    # ---- OUTPUT ----
    print("\n----- RESULTS -----")
    print(f"Original Text   : {user_text}")
    print(f"Shift Key       : {shift_key}")
    print(f"Encrypted Text  : {encrypted_text}")
    print(f"Decrypted Text  : {decrypted_text}")

    # Validation check
    if decrypted_text == user_text:
        print("\n✅ Success: Decrypted text matches the original text.")
    else:
        print("\n❌ Something went wrong - decrypted text does not match.")


if __name__ == "__main__":
    main()
