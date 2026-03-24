class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        n=len(height)
        l=0
        r=n-1
        while l<r:
            w=r-l
            h=min(height[l],height[r])
            a=w*h
            area=max(a,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return area
        
