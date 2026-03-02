Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2


class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int: 
        prevsum={}
        currsum=0
        res=0
        for i in arr:
            currsum+=i
            if currsum==k:
                res+=1
            if currsum-k in prevsum:
                res+=prevsum[currsum-k]
            prevsum[currsum]=prevsum.get(currsum,0)+1
        return res
