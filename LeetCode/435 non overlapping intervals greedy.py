class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])
        prev_end=intervals[0][1]
        c=0
        for i in range(1,len(intervals)):
            curr_end=intervals[i][1]
            curr_start=intervals[i][0]
            if prev_end>curr_start:
                c+=1
            else:
                prev_end=curr_end
        return c     
