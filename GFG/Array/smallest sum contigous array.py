class Solution:
    def smallestSumSubarray(self, A, N):
        #Your code here
        best=A[0]
        ans=A[0]
        for i in range(1,N):
            a1=best+A[i]
            a2=A[i]
            best=min(a1,a2)
            ans=min(ans,best)
        return ans
