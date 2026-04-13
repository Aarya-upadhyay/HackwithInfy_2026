class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g=defaultdict(list)
        for w in strs:
            key=''.join(sorted(w))
            g[key].append(w)
        return list(g.values())        
