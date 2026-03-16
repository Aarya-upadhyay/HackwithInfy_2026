class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        c=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                c[i]=c[i-1]+1
        for j in range(n-2,-1,-1):
            if ratings[j]>ratings[j+1]:
                c[j]=max(c[j],c[j+1]+1)
        return sum(c)
        
