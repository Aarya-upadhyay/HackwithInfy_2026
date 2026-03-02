Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        n=len(arr)
        arr.sort()
        result=[]
        for i in range(n):
            if i>0 and arr[i]==arr[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                total=arr[i]+arr[l]+arr[r]
                if total==0:
                    result.append([arr[i],arr[l],arr[r]])
                    while l<r and arr[l]==arr[l+1]:
                        l+=1
                    while l<r and arr[r]==arr[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif total<0:
                    l+=1
                else:
                    r-=1
        return result
