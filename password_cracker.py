from sys import argv
import string

alphabet = ''
alphabet += string.ascii_letters
alphabet += string.digits
alphabet += string.punctuation

"""A program that generates every possible combination of a string using '*' for unknown characters."""

script, string = argv

def first_character():
    """Returns list containing first letter or possible first letters"""
    next_letter = []
    if '*' in string[:1]:
        for letter in alphabet:
            next_letter.append(letter)
        return next_letter
    else:
        next_letter.append(string[:1])
        return next_letter

def next_character(slice1, slice2, current_letter):
    """Iterates over existing letter(s), appending all possible letter combinations"""
    next_letter = []
    if '*' in string[slice1:slice2]:
        for letter in current_letter:
            for alphabet_letter in alphabet:
                combination = f'{letter}{alphabet_letter}'
                next_letter.append(combination)
        return next_letter
    else:
        for letter in current_letter:
            existing_letter = string[slice1:slice2]
            combination = f'{letter}{existing_letter}'
            next_letter.append(combination)
        return next_letter

def main():
    """Returns an index of possible letter combinations"""
    slice1 = 1
    slice2 = 2
    current_letter = first_character()
    for i in range(len(string)):
        next_letter = next_character(slice1, slice2, current_letter)
        current_letter = next_letter
        slice1 += 1
        slice2 += 1
    for index, i in enumerate(current_letter):
        print(index, i)

main()
