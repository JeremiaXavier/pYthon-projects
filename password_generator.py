import random
import string


def password_generator(min_length, numbers=True, special_charactors=True):
    letters = string.ascii_letters  # store all letters to variable
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters+=digits
    if special_charactors:
        characters+=special

        # Checking conditions

    passwd = " "
    meet_condition = False
    has_digits = False
    has_special = False

    while not meet_condition or len(passwd) <= min_length:
        new_char = random.choice(characters)
        passwd += new_char

        if new_char in digits:
            has_digits = True
        if new_char in special:
            has_special = True


        meet_condition = True

        if numbers:
            meet_condition = has_digits
        if special_charactors:
            meet_condition  = meet_condition and has_special

    return passwd




min_length = int(input("Enter the minimum length: "))
has_number = input("Do you wand to include a number in password (y/n)").lower() == 'y'
has_special = input("do you want to include a special characters (y/n) ").lower() == 'y'

pwd = password_generator(min_length,has_number,has_special)

print("generated password is : "+pwd)

quitmessage = input("Click 'n' to exit the program: ").lower == 'n'