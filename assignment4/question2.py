#Take two matrix as input and perform the addition operation
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[9,8,7],[6,5,4],[3,2,1]]
c=[[0,0,0],[0,0,0],[0,0,0]]
#useing nested loop for addition of two matrix
for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j]=a[i][j]+b[i][j]
#printing the resultant matrix by using loop
for r in c:
    print(r)



