def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items = sorted(items, key=lambda item: item[0] / item[1], reverse=True)
    
    total_value = 0  # Total value of items in the knapsack
    for value, weight in items:
        if capacity == 0:  
            break
        
        amount = min(weight, capacity)
        total_value += amount * (value / weight)
        capacity -= amount  

    return total_value

# input is ginen
items = [(60, 10), (100, 20), (120, 30)]
capacity = 50
#calling the function fractional_knapsack and storing it in a variable result 
result = fractional_knapsack(items, capacity)
#printing the result
print(f"The maximum value that can be carried in the bag is: {result}")