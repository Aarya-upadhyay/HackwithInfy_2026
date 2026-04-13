class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        """s_map={}
        t_map={}
        for ch in s:
            s_map[ch]=s_map.get(ch,0)+1
        for ch in t:
            t_map[ch]=t_map.get(ch,0)+1
        return s_map==t_map"""
        h={}
        for ch in s:
            h[ch]=h.get(ch,0)+1
        for ch in t:
            if ch not in h or h[ch]==0:
                return False
            h[ch]-=1
        return True
                
