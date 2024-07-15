#defining the function common to find the largest prefix
def common(str1,str2):
    prefix=""
    minimum_length= min(len(str1),len(str2))
    for i in range(minimum_length):
        if str1[i]==str2[i]:
            prefix+=str2[i]
        else:
            break
    print(prefix)

#giving value to string1 and string2
str1="flower"
str2="flow"
#calling the function common 
common(str1,str2)
