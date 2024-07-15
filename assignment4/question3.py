#Write a program to find consonants in a string.
#making a function consonant to count the total no of consonants
def consonant(str1):
    count=0
    vowel="aeiouAEIOU"
    for v in str1:
        if(v.isalpha()):
            if(v not in vowel ):
                count+=1
    return count
#taking a string as input
str1=input("enter a string=")
#making a variable total_constant to store the total no of consonant
total_consonant=consonant(str1)
#printing the total no of consonant in a string
print("total consonent in a string =",total_consonant)