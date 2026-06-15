"""class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h={}
        if not nums:
            return False
        for i in nums:
            h[i]=h.get(i,0)+1
        return True if len(nums)!=len(h) else False"""

"""class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))"""

class Solution:
    def containsDuplicate(self, nums):

        seen = set()

        for num in nums:

            if num in seen:
                return True

            seen.add(num)

        return False
        
