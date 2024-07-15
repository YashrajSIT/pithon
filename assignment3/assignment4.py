# program that accepts a sentence and calculate the number of letters and digits
#making a function to count the no of alphabet and no in the string
def count(str):
    count_alphabet=0
    count_numbers=0
    for val in str:
        if(val.isalpha()):
            count_alphabet+=1
        elif(val.isdigit()):
            count_numbers+=1
    print(f"the no of alphabet and digits in string {str}={count_alphabet}and{count_numbers} ")

#taking the string input
str=input("enter the string =")
#calling the function count
count(str)
