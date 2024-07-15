#a program to find Leap year
#making a function to find out a leap year
def leapyear(year):
    if(year%4==0 and year%100!=0) or (year%400==0):
        print(f"the year {year} is a leap year")
    else:
        print(f"the year {year} is not a leap year")
#taking input of year 
year=int(input("enter the year="))
#calling the function leapyear 
leapyear(year)
