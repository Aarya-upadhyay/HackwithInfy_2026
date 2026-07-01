class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minend=nums[0]
        maxend=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            a1=minend+nums[i]
            a2=maxend+nums[i]
            a3=nums[i]
            minend=min(min(a1,a2),a3)
            maxend=max(max(a1,a2),a3)
            ans=max(max(minend,maxend),ans)
        return ans
        
