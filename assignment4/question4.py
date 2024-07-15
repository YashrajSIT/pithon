#Check if a given input number is a perfect square
#taking a function sq to find that a num is perfect square or not
def sq(num):
    if(num>=0):
        root=int(num**0.5)
        if(root*root==num):
            print(f"{num} is a perfect square")
        else:
            print(f"{num} is not a perfect square")
    else:
        print(f"{num} is not a perfect square")
#taking a number as input
num=int(input("enter the no="))
#calling a function sq
sq(num)