#find the no of alphabet in a string
#making a function to count the no of alphabet
def count(str):
    count=0
    for alpha in str:
        if(alpha.isalpha()):
            count +=1

    print(f"total no of alphabet in string {str}=",count)
            
#taking the input of string
str=input("enter a string=")
#calling the function count
count(str)






