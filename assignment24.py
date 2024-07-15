#taking input of string
str1=input("enter the string=")
#taking last index of string
index1=int(input("enter the last index of string="))
reverse=str1[index1::-1]
#printing the reverse of string
print(f"the reverse of string {str1}=",reverse)