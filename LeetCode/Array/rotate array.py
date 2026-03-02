Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]


class Solution:
    
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        n=len(arr)
        for i in range(k):
            a=arr[n-1]
            for j in range(n-1,-1,-1):
                arr[j]=arr[j-1]
            arr[0]=a
        return arr 
        n=len(arr)
        arr1=[]
        for i in range(k+1,n-1):
            arr1.append(arr[i])
        b=n-1
        for i in range(k,-1,-1):
            arr[b]=arr[i]
            b-=1
        c=0
        for i in range(k):
            arr[c]=arr1[i]
            c+=1
        return arr """
      
        n = len(arr)
        k = k % n   # very important
        
        def reverse(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        
        # Step 1: Reverse whole array
        reverse(0, n - 1)
        
        # Step 2: Reverse first k elements
        reverse(0, k - 1)
        
        # Step 3: Reverse remaining elements
        reverse(k, n - 1)
