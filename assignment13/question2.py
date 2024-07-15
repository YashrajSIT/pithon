def convert_case(s):
    # Convert the string to uppercase
    upper_case = ''.join(map(str.upper, s))
    
    # Convert the string to lowercase
    lower_case = ''.join(map(str.lower, s))
    
    return upper_case, lower_case

# taking input
input_string = input("enter a string=")
upper, lower = convert_case(input_string)

print("Upper case:", upper)
print("Lower case:", lower)