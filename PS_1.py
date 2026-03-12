# O(n2) Brute Force
def solve(arr):
    types=set(arr)
    best_count=0
    best_type=float('inf')
    for t in types:
        last_picked=-2
        c=0
        for i in range(len(arr)):
            if arr[i]==t and i-last_picked>1:
                c+=1
                last_picked=i
        if c>best_count or (c==best_count and t<best_type):
            best_count=c
            best_type=t
    return best_type
arr=[1,2,2,1,2,1,1,1,1]
a=solve(arr)
print(a)

#optimal approach O(n)


    
