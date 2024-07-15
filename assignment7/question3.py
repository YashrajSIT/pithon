#taking input of sides of triangle
a=float(input("enter the  1st side of triangle="))
b=float(input("enter the 2nd side of triangle="))
c=float(input("enter the 3rd side of triangle="))
hypotenus=0
#checking  triangle is valid or not
if(a+b>c or b+c>a or c+a>b):
    print(f"{a},{b},{c} is a valid triangle")
else:
    print("not a valid triangle")

#to find the type of triangle
if(a==b==c):
    print("a,b,c is an equilateral triangle")
elif(a==b or b==c or c==a):
    print("a,b,c is an isoceles triangle")
else:
    print("a,b,c is a scalene triangle")

#to check right angled triangle
if (a>b and a>c and(a**2==b**2+c**2)):
    print("it ia right angle triangle")
    hypotenus=a**2
elif (b>c and b>a and(b**2==a**2+c**2)):
    print("it is a right angle triangle")
    hypotenus=b**2
elif (c>a and c>b and (c**2==a**2+b**2)):
    print("it is a right angle triangle")
    hypotenus=c**2
else:
    print("not right angle triangle")

#to finnd circumradius
if hypotenus:
    circumradius=hypotenus/2
    print(f"circumradius is ={circumradius}")
else:
    print("no a right angle triangle")