#making a function solvedpuzzel to calculate the no of chicken and rabbit
def solvedpuzzel(total_head,total_legs):
    for no_of_chicken in range(total_head+1):
        no_of_rabbit=total_head-no_of_chicken
        #if 2*no of chicken because chicken have 2 legs and 4*rabbit because rabbit have 4 legs
        #if 2*no_of_chicken +4*no_of_rabbit==total_no_of_legs then return no of chicken and no of rabbit
        if 2*no_of_chicken+4*no_of_rabbit==total_legs:
            return no_of_chicken,no_of_rabbit

total_head=35
total_legs=94
#calling the function solvedpuzzel to calculate the no of chicken and rabbit 
solution=solvedpuzzel(total_head,total_legs)
if solution:
    chickens,rabbits=solution
    print(f"total no of chicken={chickens}")
    print(f"total no of rabbits={rabbits}")
else:
    print("no solution")
