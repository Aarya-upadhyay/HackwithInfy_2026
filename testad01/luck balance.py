def luckBalance(k, contests):
    # Write your code here
    imp=[]
    luck=0
    for l,t in contests:
        if t==0:
            luck+=l
        else:
            imp.append(l)
    imp.sort(reverse=True)
    luck+=sum(imp[:k])
    luck-=sum(imp[k:])
    return luck
