
def largestRectangle(h):
    # Write your code here
    n=len(h)
    stk=[]
    max_area=0
    for i in range(n):
        while stk and h[i]<h[stk[-1]]:
            hi=h[stk.pop()]
            if not stk:
                w=i
            else:
                w=i-stk[-1]-1
            max_area=max(max_area,hi*w)
        stk.append(i)
    while stk:
        hi=h[stk.pop()]
        if not stk:
            w=n
        else:
            w=n-stk[-1]-1
        max_area=max(max_area,hi*w)
    return max_area
