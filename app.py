import string
import random


letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation


def password_length():

    length = input("Input the size that you want your password: ")

    try:
        length = int(length)
        return length
    except ValueError:
        print("That is not an integer number")


def generate_password(size=8):
    joined = f'{letters}{numbers}{punctuation}'

    # converting to a list
    joined = list(joined)

    # shuffling list 
    random.shuffle(joined)

    random_password = random.choices(joined, k=size)
    random_password = ''.join(random_password)
    return random_password


size = password_length()
password = generate_password(size)
print("Here is your total safe password: ", password)

