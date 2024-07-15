#program to find distance between two points
#taking the coordinate of point1
x1=int(input("enter x coordinate point1="))
y1=int(input("enter y coordinate of point1="))
#taking the coordinate of point2
x2=int(input("enter x coordinate of point2="))
y2=int(input("enter x coordinate of point2="))
#we calculte the distance b\w two point by applying the formula ((x2-x1)^2+(y2-y1)^2)^1\2
print("distance between point 1 and point 2=", ((x2-x1)**2+(y2-y1)**2)**0.5)