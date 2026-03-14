
def climbingLeaderboard(ranked, player):
    # Write your code here
    unique=[]
    for score in ranked:
        if not unique or unique[-1]!=score:
            unique.append(score)
    n=len(unique)
    res=[]
    j=n-1
    for i in player:
        while j>=0 and i>=unique[j]:
            j-=1
        res.append(j+2)
    return res
        
    
