#
# File   : CHOJY083_encryptor.py
# Author : Joon Choi
# Stud ID: 110457036
# Email ID: CHOJY083
# Description: Programming Assignment 2 - Caesar Cipher
# This is my own work as defined by the University's Academic Misconduct Policy.

# -------------------- FUNCTIONS --------------------

# Display program details and author information
def display_details():
    """Display student and assignment details"""
    print("File   : CHOJY083_encryptor.py")
    print("Author : Joon Choi")
    print("Stud ID: 110457036")
    print("Email ID : CHOJY083")
    print("Description: Programming Assignment 2 - Caesar Cipher")
    print("This is my own work as defined by the University's Academic Misconduct Policy.\n")

# Display the menu and return the user's validated choice
def get_menu_choice():
    """Show menu, validate input (1–4), return int choice"""
    print("*** Menu ***")
    print("1. Encrypt string")
    print("2. Decrypt string")
    print("3. Brute force decryption")
    print("4. Quit")
    choice = input("What would you like to do [1,2,3,4]? ")
    while choice not in ["1", "2", "3", "4"]:
        print("Invalid choice, please enter either 1, 2, 3 or 4.")
        choice = input("What would you like to do [1,2,3,4]? ")
    return int(choice)


# Get a valid integer offset from the user
def get_offset():
    """Prompt for offset, validate 1–94, return int offset"""
    offset = input("Please enter offset value (1 to 94): ")
    while not offset.isdigit() or not (1 <= int(offset) <= 94):
        offset = input("Please enter offset value (1 to 94): ")
    return int(offset)


# Encrypt a string using Caesar cipher with the given offset
def encrypt_string(text, offset):
    """Encrypt text using Caesar Cipher with ASCII 32-126 wraparound"""
    result = ''
    for ch in text:
        ascii_val = ord(ch)                   # Convert char to ASCII
        new_ascii = ascii_val + offset        # Shift forward
        if new_ascii > 126:                   # Wraparound if beyond 126
            new_ascii = 32 + (new_ascii - 127)
        result += chr(new_ascii)              # Convert back to char
    return result


# Decrypt a string using Caesar cipher with the given offset
def decrypt_string(text, offset):
    """Decrypt text using Caesar Cipher with ASCII 32-126 wraparound"""
    result = ''
    for ch in text:
        ascii_val = ord(ch)                   # Convert char to ASCII
        new_ascii = ascii_val - offset        # Shift backwards
        if new_ascii < 32:                    # Wraparound if below 32
            new_ascii = 127 - (32 - new_ascii)
        result += chr(new_ascii)              # Convert back to char
    return result


# Brute force decrypt a string by trying all possible offsets
def brute_force_decrypt(text):
    """Attempt all 94 offsets for Caesar Cipher decryption"""
    print("Brute force results:\n")
    for offset in range(1, 95):  # 1 to 94
        result = ''
        for ch in text:
            ascii_val = ord(ch)
            new_ascii = ascii_val - offset
            if new_ascii < 32:  # Wraparound if below 32
                new_ascii = 127 - (32 - new_ascii)
            result += chr(new_ascii)
        print(f"Offset: {offset} = Decrypted string: {result}")
    print()  # Extra line for spacing


# -------------------- MAIN PROGRAM --------------------

# Main program control loop
def main():
    display_details()

    choice = 0
    while choice != 4:  # no break/exit; ends naturally on 4
        choice = get_menu_choice()

        if choice == 1:
            text = input("Please enter string to encrypt: ")
            offset = get_offset()
            encrypted = encrypt_string(text, offset)
            print("Encrypted string:\n")
            print(encrypted + "\n")

        elif choice == 2:
            text = input("Please enter string to decrypt: ")
            offset = get_offset()
            decrypted = decrypt_string(text, offset)
            print("Decrypted string:\n")
            print(decrypted + "\n")

        elif choice == 3:
            text = input("Please enter string to brute force decrypt: ")
            brute_force_decrypt(text)

    print("Goodbye.")


# -------------------- RUN PROGRAM --------------------
main()

