#!/usr/bin/python3
import string
import sys
# Constants
MAX_KEY_SIZE = 26
ALPHABET = (string.ascii_uppercase)
alphabet = (string.ascii_lowercase)
PUNCTUATION = string.punctuation
USAGE_MESSAGE = "\n./caesar_ciher.py (e/d) <shift> (<text>|--file <infile>) [--write <outfile>]"
Exanple_message = "\n./caesar_cipher.py e <shift> <text> \n./caesar_cipher.py d <shift> <text> \n./caesar_cipher.py e <shift> -- file <filename> \n./caesar_cipher.py d <shift> --file <filename>"


"""
User input functions
"""

def print_usage():
    print("usage: ", USAGE_MESSAGE)
    print(" ")
    print("Examples: ", Exanple_message)
    quit()

def get_cipher_mode():
    """
    Gets user input for the cipher mode. Must be either encrypt, e, decrypt or d.
    
    Returns cipher_mode as a string.
    """
    while True:
        cipher_mode = input("Do you wish to encrypt or decrypt? ").lower()
        if cipher_mode in "encrypt e decrypt d".split():
            return cipher_mode
        else:
            print("Enter either 'encrypt' or 'e' or 'decrypt' or 'd'. ")


def get_shift_value():
    """
    Gets user input for the shift value. Must be a positive integer.
    
    Returns shift_value as an int.
    """
    while True:
        shift_value = input("Enter the shift value: ")
        if not shift_value.isdigit():
            print("Enter a positive integer")
        elif int(shift_value) < 0:
            print("Enter a positive integer")
        else:
            return int(shift_value)


def get_msg():
    """
    Gets user input for the text. It continues reading in input until the user
    inputs an empty line (i.e. double enter).
    """
    line = input("Enter your message:")
    msg = ""

    while line != "":
        msg += line
        line = input()

    return msg

"""
File usage functions
"""

def ret_file_msg(file_name):
    f = open(file_name, "r")
    s = f.read()
    print(s)
    f.close()
    pass

def write_msg_to_file(file_name, msg):
    f = open(file_name,"a")
    f.write(msg)
    f.close()
    pass
    
"""
Cipher functions
"""

def translate_msg(shift_value, msg):
    """
    Performs the Caesar cipher on a string converted to upper case with the given shift.
    
    shift_value : int
        shift amount/rotation value for the cipher. Positive encrypts and negative decrypts.
    msg : str
        message to be translated
    
    Returns the translated message as a string.
    """
    translated_msg = ''

    for symbol in msg:
        # Need to check Symbol is a letter
        if symbol in ALPHABET:
            position = ALPHABET.index(symbol)
            new_symbol = ALPHABET[(position + shift_value) % MAX_KEY_SIZE]
            translated_msg += new_symbol
        elif symbol in alphabet:
            position = alphabet.index(symbol)
            new_symbol = alphabet[(position + shift_value) % MAX_KEY_SIZE]
            translated_msg += new_symbol
        else:
            # Leave Symbol unchanged if it's not a letter
            translated_msg += symbol

    return translated_msg

def caesar_encrypt(shift_value, msg):
    """
    Wrapper function for translate_msg
    
    N.B. shift value kept positive for encryption.
    """
    return translate_msg(shift_value, msg)
    

def caesar_decrypt(shift_value, msg):
    """
    Wrapper function for translate_msg
    
    N.B. shift value becomes negative for decryption.
    """
    return translate_msg(-shift_value, msg)

"""
Main function
"""
def main(args):
    if len(args) < 4:
        print_usage()
    mode = args[1]
    shift = int(args[2])
    if mode == "e":
        if args[-2] == "--write":
            msg = caesar_encrypt(shift, " ".join(args[3:-2]))
            write_msg_to_file(args[-1], msg)
        elif args[-2] == "--file":
            caesar_encrypt(shift, " ".join(args[3:-2]))
            ret_file_msg(args[-1])
        else:
            print(caesar_encrypt(shift, " ".join(args[3:])))
    elif mode == "d":
        if args[-2] == "--write":
            msg = caesar_decrypt(shift, " ".join(args[3:-2]))
            write_msg_to_file(args[-1], msg)
        elif args[-2] == "--file":
            caesar_decrypt(shift, " ".join(args[3:-2]))
            ret_file_msg(args[-1])
        else:
            print(caesar_decrypt(shift, " ".join(args[3:])))
    else:
        print_usage()


if __name__ == '__main__':
    main(sys.argv)

