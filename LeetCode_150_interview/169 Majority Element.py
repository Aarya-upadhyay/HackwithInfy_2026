from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """c=0
       
        cand=None
        for i in nums:
            if c==0:
                cand=i
            if cand==i:
                c+=1
            else:
                c-=1
        return cand
        """
        #hash map using counter func that returns the count of each elem as freq dict obj
        count=Counter(nums)
        n=len(nums)
        for i in count:
            if count[i]>n//2:
                return i

        
