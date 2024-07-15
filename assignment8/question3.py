#calling a function find_winner
def find_winner(votes):
    vote_count={}
    for candidate in votes:
        if candidate in vote_count:
            vote_count[candidate]+=1
        else:
            vote_count[candidate]=1
    
    maximumvote=0

    winner=None
    for candidate,count in  vote_count.items():
     if count>maximumvote:
            maximumvote=count
            winner=candidate
    #returning the winner 
    return winner
#input of votes
votes=["a","b","a","c","a"]
#calling a function find_winner and storing its value in variable winner 
winner=find_winner(votes)
#printing the winner
print(winner)
