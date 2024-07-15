
#making a function to find substring present or not
def substring(str,sub_string):
    length_substring=len(sub_string)
    for i in range(len(str)-length_substring+1):
        if str[i:i+length_substring]==sub_string:
            return True
    return False
#taking input of string
str=input("enter the string=")
#taking sub_string input
sub_string=input("enter the substring you want to find =")
if substring(str,sub_string):
    print(f"substring {sub_string} is found ")
else:
    print(f"substring {sub_string} not found")