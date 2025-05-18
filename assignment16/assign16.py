import string 
import random


def generate_passwords():
    lowercase = string.ascii_lowercase
    # print(lowercase)    
    uppercase = string.ascii_uppercase
    # print(uppercase)
    digits = string.digits
    # print(digits)
    special_characters = string.punctuation
    # print(special_characters)

    pass1 = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    
    all_characters = uppercase + lowercase + digits + special_characters
    pass1 += random.choices(all_characters, k= len_password - 4)

    random.shuffle(pass1)

    return ''.join(pass1)


len_password = int(input("Enter the length of the password: "))

if len_password < 4:
    print("Password length should be at least 4")   

else:
    pass1 = generate_passwords()
    print("Password 1: ", pass1)