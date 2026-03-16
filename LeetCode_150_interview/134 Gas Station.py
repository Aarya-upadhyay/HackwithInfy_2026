def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        if sum(gas) < sum(cost):
            return -1
        start=0
        tank=0
        total=0
        for i in range(n):
            g,c=gas[i],cost[i]
            tank+=g-c
            if tank<0:
                start=i+1
                tank=0
                
        return start
       
        
