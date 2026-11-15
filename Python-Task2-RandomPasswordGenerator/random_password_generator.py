import string
import secrets

print("=== Random Password Generator ===")

length = int(input("Enter password length (minimum 8): "))

if length < 8:
    print("Password must be at least 8 characters.")

else:
    uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    numbers = input("Include numbers? (y/n): ").lower() == "y"
    symbols = input("Include symbols? (y/n): ").lower() == "y"

    characters = ""
    password = []

    if uppercase:
        characters += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))

    if lowercase:
        characters += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))

    if numbers:
        characters += string.digits
        password.append(secrets.choice(string.digits))

    if symbols:
        characters += string.punctuation
        password.append(secrets.choice(string.punctuation))

    if not characters:
        print("Select at least one character type.")

    elif len(password) > length:
        print("Password length is too short for selected options.")

    else:
        while len(password) < length:
            password.append(secrets.choice(characters))

        secrets.SystemRandom().shuffle(password)

        final_password = "".join(password)

        print("\nGenerated Password:", final_password)
        print("Password Length:", len(final_password))