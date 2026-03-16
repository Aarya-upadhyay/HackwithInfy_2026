
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
