import secrets
import string

def generate_password(length=12):
    # Define the character sets
    alphabet = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# Example usage: Generate a 16-character password
print(generate_password(16))
