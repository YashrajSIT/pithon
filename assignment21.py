#program that takes a string and an index as input and prints the char at that index
#first take a input string
str1=input("enter a string= ")
#taking a index 
index=int(input("enter the index="))
#storing the index in the variable ch
ch=str1[index]
#printing the character
print(f"the character at index {index}=",ch)