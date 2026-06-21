class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        max_len=0
        h={}
        for i in range(len(s)):
            h[s[i]]=h.get(s[i],0)+1
            while (i-l+1)-max(h.values())>k:
                h[s[l]]-=1
                if h[s[l]]==0:
                    del h[s[l]]
                l+=1
            max_len=max(max_len,i-l+1)
        return max_len
