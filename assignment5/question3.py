
# Input a comma separated list from console. Write a program to print this list 
#after removing all duplicate values with original order reserved. 
def duplicate(str1):
#split the str1 into a list of values
    item=str1.split(',')
    #create a new list to store unique value
    newitem=[]
    for items in item:
        stripped_item=items.strip()
        if stripped_item not in newitem:
            newitem.append(stripped_item)
    return newitem
#taking input of string
str1=input("enter a comma seperated list=")
#calling function and storing the return the value in str2 
str2=duplicate(str1)
#printing the result
print(" list after removing all duplicate values with original order reserved.")
print(str2)
