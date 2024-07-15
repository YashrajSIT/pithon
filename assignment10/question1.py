def is_palindrome(word):
    # Base case: If the word is empty or has only one character, it's a palindrome
    if len(word) <= 1:
        return True
    
    # Check the first and last characters
    if word[0] != word[-1]:
        return False
    
    # Recursively check the substring excluding the first and last characters
    return is_palindrome(word[1:-1])

# Example usage
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False