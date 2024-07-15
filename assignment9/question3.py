def calculate_discounted_price(original_price, discount_percent):
    # Calculate the discount amount
    discount_amount = (original_price * discount_percent) / 100
    # Calculate the final price after applying the discount
    discounted_price = original_price - discount_amount
    return discounted_price

# Input the original price from the user
original_price = float(input("Enter the original price of the product: "))

# Input the discount percentage from the user
discount_percent = int(input("Enter the discount percentage: "))

# Call the function and print the result
discounted_price = calculate_discounted_price(original_price, discount_percent)
print(f"The discounted price is: {discounted_price:.2f}")