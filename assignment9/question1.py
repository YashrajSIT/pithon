def calculated_stats(numbers):
    if not numbers:
        return None,None,None
    minimum=min(numbers)
    maximum=max(numbers)
    avg=sum(numbers)/len(numbers)
    return minimum,maximum,avg

userinput=input("enter numbers seprated by space:")
numbers=list(map(float,userinput.split()))
min_val,max_val,avg_val=calculated_stats(numbers)
print(f"minimum={min_val},maximum={max_val},average={avg_val}")