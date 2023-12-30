import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length_input = input("Enter the desired length of the password: ")

    if length_input.isdigit():
        length = int(length_input)
        if length > 0:
            password = generate_password(length)
            print("Generated Password:", password)
        else:
            print("Please enter a valid positive length.")
    else:
        print("Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
