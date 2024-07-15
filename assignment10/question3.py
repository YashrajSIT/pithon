def sum_of_digits(num):
    # Base case: If num is a single digit, return the number itself
    if num < 10:
        return num
    
    # Recursive case: Sum the last digit and the sum of the remaining digits
    return num % 10 + sum_of_digits(num // 10)

# Taking user input
user_input = int(input("Enter an integer: "))
result = sum_of_digits(user_input)
print(f"The sum of the digits is: {result}")