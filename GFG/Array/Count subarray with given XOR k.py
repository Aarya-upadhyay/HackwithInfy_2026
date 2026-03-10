class Solution:
    def subarrayXor(self, arr, k):
        # code here
        c=0
        pre=0
        h={}
        for i in arr:
            pre^=i
            if pre==k:
                c+=1
            if pre^k in h:
                c+=h[pre^k]
            h[pre]=h.get(pre,0)+1
        return c
                
