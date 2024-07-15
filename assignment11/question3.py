from collections import Counter

def are_anagrams_counter(str1, str2):
    # Check if lengths are the same
    if len(str1) != len(str2):
        return False
    # Count and compare
    return Counter(str1) == Counter(str2)

# Get user input
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Check if the strings are anagrams
if are_anagrams_counter(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")