You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.



class Solution:
    def findMaxAverage(self, arr: List[int], k: int) -> float:
        n=len(arr)
        max_sum=float('-inf')
        sum=0
        for i in range(k):
            sum+=arr[i]
        max_sum=max(max_sum,sum)
        for i in range(k,n):
            sum+=arr[i]-arr[i-k]
            max_sum=max(max_sum,sum)
        return max_sum/k
       
        """s = sum(nums[:k])
        m = s
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            if s > m:
                m = s
        return m / float(k)"""
