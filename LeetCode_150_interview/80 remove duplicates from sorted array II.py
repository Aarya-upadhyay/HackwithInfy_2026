class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
       
        n=len(arr)
        if n<=2:
            return n
        j=2
        for i in range(2,n):
            if (arr[i]!=arr[j-2]):
                arr[j]=arr[i]
                j+=1
        return j
