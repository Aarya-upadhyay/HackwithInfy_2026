class Solution:
    def segregate0and1(self, arr):
        # code here
        l=0
        r=len(arr)-1
        while l<r:
            if arr[l]==0:
                l+=1
            elif arr[r]==1:
                r-=1
            else:
                arr[l],arr[r]=arr[r],arr[l]
           
                l+=1
                r-=1
        return arr
        
