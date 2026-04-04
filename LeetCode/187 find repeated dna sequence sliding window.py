class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = {}
        res = []
        n = len(s)
        
        for i in range(n - 9):   # window size = 10
            sub = s[i:i+10]
            
            seen[sub] = seen.get(sub, 0) + 1
            
            if seen[sub] == 2:   # add only once when it becomes repeated
                res.append(sub)
        
        return res
