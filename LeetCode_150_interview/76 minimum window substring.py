class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        n=len(s)
        m=len(t)
        freq={}
        for i in t:
            freq[i]=freq.get(i,0)+1
        res=[-1,-1]
        res_len=float("inf")
        win_map={}
        have=0
        l=0
        need=len(freq)
        for r in range(n):
            c=s[r]
            win_map[c]=win_map.get(c,0)+1
            if c in freq and freq[c]==win_map[c]:
                have+=1
            while have==need:
                if (r-l+1)<res_len:
                    res=[l,r]
                    res_len=r-l+1
                win_map[s[l]]-=1
                if s[l] in freq and win_map[s[l]]<freq[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if res_len != float('inf') else ""

