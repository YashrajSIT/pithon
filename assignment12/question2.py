import random
import string

def random_alphabetic_char():
    """Generate a random alphabetical character."""
    return random.choice(string.ascii_letters)

def random_alphabetic_string(length):
    """Generate a random alphabetical string of arbitrary length."""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def random_fixed_length_string(length):
    """Generate a random alphabetical string of fixed length."""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# Example usage:
print(random_alphabetic_char())  # Generates a random alphabetical character
print(random_alphabetic_string(10))  # Generates a random alphabetical string of length 10
print(random_fixed_length_string(5))  # Generates a random alphabetical string of fixed length 