import re

def check_password_strength(password):
    # Initialize strength score
    strength = 0

    # Check length
    if len(password) < 8:
        return "Weak Password: Must be at least 8 characters long."

    # Check for character types
    if re.search(r'[A-Z]', password):  # Uppercase letters
        strength += 1
    if re.search(r'[a-z]', password):  # Lowercase letters
        strength += 1
    if re.search(r'[0-9]', password):  # Numbers
        strength += 1
    if re.search(r'[^A-Za-z0-9]', password):  # Symbols
        strength += 1

    # Evaluate strength based on score
    if strength < 3:
        return "Weak Password: Must contain at least 3 different character types (uppercase, lowercase, numbers, symbols)."

    if len(password) >= 12 and strength == 4:
        return "Very Strong Password"
    elif len(password) >= 10 and strength == 4:
        return "Strong Password"
    elif len(password) >= 8 and strength >= 3:
        return "Moderate Password"

    return "Weak Password: Consider using more characters or different types."

def main():
    print("Welcome to the Password Strength Checker!")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Exiting the Password Strength Checker. Stay secure! & Always prefer strong and different passwords for multiple accounts to stay safe")
            break

        result = check_password_strength(password)
        print(result)

if __name__ == "__main__":
    main()