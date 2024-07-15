#program to find the gcd of two no
#create a function find gcd
def find_gcd(x,y):
    if y==0:
        return x
    return find_gcd(y,x%y)

#taking input of two no
a=int(input("enter first number:"))
b=int(input("enter second number:"))
#calling function to find the gcd
gcd=find_gcd(a,b)
#printing the value of gcd
print("gcd of two no is:",gcd)