import heapq

def runningMedian(a):
    low = []  # Max-heap (lower half)
    high = [] # Min-heap (upper half)
    res = []
    
    for x in a:
        # 1. Push to low heap (invert sign for max-heap behavior)
        heapq.heappush(low, -x)
        
        # 2. Balance: Move the largest of 'low' to 'high'
        heapq.heappush(high, -heapq.heappop(low))
        
        # 3. Keep 'low' equal or 1 element larger than 'high'
        if len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))
            
        # 4. Calculate Median
        if len(low) > len(high):
            # Odd number: middle is in 'low'
            res.append(float(-low[0]))
        else:
            # Even number: average of both tops
            res.append((-low[0] + high[0]) / 2.0)
            
    return res
