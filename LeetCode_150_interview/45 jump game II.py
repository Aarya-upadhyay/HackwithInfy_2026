class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        curr_end=0
        far=0
        j=0
        for i in range(n-1):
            far=max(far,i+nums[i])
            if i==curr_end:
                j+=1
                curr_end=far
        return j
        
