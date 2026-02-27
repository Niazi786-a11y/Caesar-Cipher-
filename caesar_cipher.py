# Function to encrypt text using Caesar Cipher
def caesar_encrypt(text, shift):
    # empty string to store result
    result1 = ""

    for char in text:

        # Check if character is uppercase letter
        if char.isupper():
            result1 += chr((ord(char) - 65 + shift) % 26 + 65)

        # Check if character is lowercase letter
        elif char.islower():
            result1 += chr((ord(char) - 97 + shift) % 26 + 97)

        # If not a letter, keep it same
        else:
            result1 += char

    return result1


# Function to decrypt text using Caesar Cipher
def caesar_decrypt(Text, shift):
    result2 = ""

    for char in Text:
        if char.isupper():
            result2 += chr((ord(char) - 65 - shift) % 26 + 65)

        elif char.islower():
            result2 += chr((ord(char) - 97 - shift) % 26 + 97)

        else:
            result2 += char

    return result2


# Taking input from user
info = input("Enter your information: ")
sh_value = int(input("Enter Shift Value: "))

# Encrypting Information
encrypted = caesar_encrypt(info, sh_value)
print("Encrypted Info:", encrypted)

# Decrypting Information
decrypted = caesar_decrypt(encrypted, sh_value)
print("Decrypted Info:", decrypted)