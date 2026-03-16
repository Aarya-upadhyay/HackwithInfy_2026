class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """res=[]
        for i in range(len(nums)):
            prod=1
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    continue
                prod*=nums[j]
            res.append(prod)
        return res"""
        n=len(nums)
        pre=1
        suf=1
        res=[1]*n
        for i in range(n):
            res[i]=pre
            pre*=nums[i]
        for j in range(n-1,-1,-1):
            res[j]*=suf
            suf*=nums[j]
        return res

        
