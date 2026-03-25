class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        l=0
        min_count=float('inf')
        curr_sum=0
        for i in range(n):
            curr_sum+=nums[i]
            while curr_sum>=target:
                min_count=min(min_count,i-l+1)
                curr_sum-=nums[l]
                l+=1
        return 0 if min_count==float('inf') else min_count
