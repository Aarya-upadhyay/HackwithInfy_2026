# STRIVER
arr.sort()
        n=len(arr)
        l=[]
        for i in range(1,n):
            if arr[i]==arr[i-1]:
                l.append(arr[i])
                break
        xor_all=0
        xor_num=0
        for i in range(1,n+1):
            xor_all^=arr[i]
        for j in arr:
            xor_num^=j
        l.append(xor_all^xor_num)
        return l
