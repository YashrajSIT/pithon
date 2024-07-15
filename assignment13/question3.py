def sort_by_first_value(lst):
    return sorted(lst, key=lambda x: x[0])

# Example input
input_list = [[5, 7], [9, 11], [7, 3], [0, 12]]

# Sort the list
sorted_list = sort_by_first_value(input_list)

print("Sorted list:", sorted_list)