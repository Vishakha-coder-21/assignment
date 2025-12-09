import random
import string

def generate_password(words):
    word = random.choice(words).capitalize()       
    number = random.choice(string.digits)          
    special = random.choice("!@#$%^&*")         

    password = word + number + special


    while len(password) < 8:
        password += random.choice(string.ascii_letters + string.digits + "!@#$%^&*")

    return password

try:
    uid = input("Enter User ID: ")
    name = input("Enter Name: ")
    words = input("Enter words separated by space: ").split()

    if len(words) == 0:
        raise Exception("Enter at least one word!")

    password = generate_password(words)

    # store details in dictionary
    user_data = {
        "User ID": uid,
        "Name": name,
        "Password": password
    }

    print("\nUser Details Stored in Dictionary:")
    print(user_data)

    print("Generated Password:", password)

except Exception as e:
    print("Error:", e)
