🔐 Project 2: Basic Encryption & Decryption (Caesar Cipher)

A Python-based Caesar Cipher tool that encrypts and decrypts text using
a simple shift-based substitution technique, demonstrating the
fundamentals of data confidentiality.

Goal

Implement a simple encryption and decryption technique.

Features

* Encrypts user text using a Caesar Cipher shift
* Decrypts the encrypted text back to the original
* Displays both encrypted and decrypted output
* Validates that decryption matches the original text
* Handles spaces, numbers, and punctuation as edge cases (left unchanged)

How It Works

The Caesar Cipher shifts each letter of the alphabet by a fixed number
of positions (the key).

Encryption formula:
```
E(x) = (x + n) mod 26
```

Decryption formula:
```
D(x) = (x - n) mod 26
```

Where x is the character's position in the alphabet (A=0, B=1, ... Z=25)
and n is the shift key.

Technologies Used

* Python 3

How to Run

```
python caesar_cipher.py
```

Example

```
Enter the text you want to encrypt: HELLO PAKISTAN
Enter the shift key (e.g., 3): 3

----- RESULTS -----
Original Text   : HELLO PAKISTAN
Shift Key       : 3
Encrypted Text  : KHOOR SDNLVWDQ
Decrypted Text  : HELLO PAKISTAN

✅ Success: Decrypted text matches the original text.
```

Screenshot

![Caesar Cipher Output](screenshot.png)

Key Learnings

* Encryption/decryption logic building
* ASCII to character conversion (ord() and chr())
* Modular arithmetic for wrap-around alphabet handling
* Edge case handling (spaces, numbers, punctuation left unchanged)

Limitation

The Caesar Cipher is not secure for real-world use — it has only 25
possible keys and preserves letter-frequency patterns, making it easily
breakable via brute force or frequency analysis. It is used here purely
for learning the core concepts of encryption before moving to
stronger algorithms (like AES).

Author
Ahtasham Ul Haq
BS Cyber Security Student
UET Taxila

Project
This project was created as part of the DecodeLabs Cyber Security Internship.
