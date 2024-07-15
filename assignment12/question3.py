import random

def generate_random_integers_list(size, min_val, max_val):
    """Generate a list of random integers."""
    return [random.randint(min_val, max_val) for _ in range(size)]

def select_random_items(lst, k):
    """Randomly select k items from a list."""
    return random.sample(lst, k)

# Example usage:
# Generate a list of 20 random integers between 1 and 100
random_list = generate_random_integers_list(20, 1, 100)
print("Generated list:", random_list)

# Select 5 random items from the generated list
selected_items = select_random_items(random_list, 5)
print("Randomly selected items:", selected_items)