#. Check if a user input string is palindrome.
#making a function to cheack a string is palindrome or not
def palindrome(str1):
    str2=str1[len(str1)::-1]
    if(str1==str2):
        print(f"string {str1} is palindrome")
    else:
        print(f"string {str1} is not palindrome")
        
#taking a string as input
str1=input("enter a string=")
#last_index=int(input(""))
#calling the function palindrome
palindrome(str1)


