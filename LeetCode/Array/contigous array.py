Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


  class Solution:
    def findMaxLength(self, arr: List[int]) -> int:
        prefixsum=0
        hashmap={0:-1}
        maxlen=0
        for i in range(len(arr)):
            if arr[i]==0:
                prefixsum+=-1
            else:
                prefixsum+=1
            if prefixsum in hashmap:
                length=i-hashmap[prefixsum]
                maxlen=max(length,maxlen)
            else:
                hashmap[prefixsum]=i
        return maxlen
        
