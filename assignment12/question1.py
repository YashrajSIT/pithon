import random

def roll_dice(num_rolls):
    # Initialize the count for each face of the dice
    counts = {i: 0 for i in range(1, 7)}

    # Roll the dice num_rolls times
    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        counts[roll] += 1

    return counts

def print_counts(counts):
    # Print the results
    for face, count in counts.items():
        print(f"Face {face} appeared {count} times")

# Roll the dice 500 times
dice_counts = roll_dice(500)
print_counts(dice_counts)