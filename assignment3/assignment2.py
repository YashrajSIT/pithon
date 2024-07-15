#a program that can accept two strings as input and print the string with maximum length
#making a function to find the string of maximum length 
def maxstring(str1,str2):
    if(len(str1)>len(str2)):
        print("string with maximum length= ",str1)
    elif(len(str2)>len(str1)):
        print("string with maximum length= ",str2)
    else:
        print(f"both string {str1} and {str2} are of same lenght")
#taking input of string1
str1=input("enter the first string=")
#taking input of string2
str2=input("enter the second string=")
#calling a function to find the string of max length
maxstring(str1,str2)

