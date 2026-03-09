from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # counter 
        k=Counter(nums)
        l=[]
        for i in k:
            if k[i]>(len(nums)//3):
                l.append(i)
        return l
        
