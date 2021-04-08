import string
import random


letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation


# get the password length desired
def password_length():

    length = input("Input the size that you want your password: ")

    try:
        length = int(length)
        return length
    except ValueError:
        print("That is not an integer number")


# ask user the types of characters he wants
def get_types():

    choice_letters = input("Want letters?(true/false): ")
    choice_numbers = input("Want numbers?(true/false): ")
    choice_punctuation = input("Want punctuation?(true/false): ")

    try:
        choice_letters = eval(choice_letters.title())  # tries to convert true to a bool = True
        choice_numbers = eval(choice_numbers.title())
        choice_punctuation = eval(choice_punctuation.title())
        
        return [choice_letters, choice_numbers, choice_punctuation]
    except NameError:
        print("You can only input y or n")
        print("Defaulting that you want everything")
    
    return [True, True, True]  # defaults to this is there is an error


# gets the array returned by function above and creates and creates a string with the desired values
def generate_string(choice_list):

    password_string = ''
    password_string += letters if choice_list[0] else '' 
    password_string += numbers if choice_list[1] else ''
    password_string += punctuation if choice_list[2] else ''

    return password_string


def generate_password(choice_list, size=8):

    # converting to a list
    password_string = generate_string(choice_list)
    password_string = list(password_string)

    # shuffling list 
    random.shuffle(password_string)

    random_password = random.choices(password_string, k=size)
    random_password = ''.join(random_password)
    return random_password


size = password_length()  # getting size of password
choice_list = get_types()  #  getting the list with values true or false based on user choice
password = generate_password(choice_list, size)  # generated password with list and size

print("Your total safe password: ", password)
