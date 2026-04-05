class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    if abs(i-j)<=k:
                        return True
        return False"""
        n=len(nums)
        l=0
        win=set()
        for i in range(n):
            if nums[i] in win:
                return True
            win.add(nums[i])
            if i-l >=k:
                win.remove(nums[l])
                l+=1
        return False

