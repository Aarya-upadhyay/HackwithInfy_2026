class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """j=0
        for i in range(len(s)):
            for _ in range(len(t)):
                if j<len(t):
                    if s[i]==t[j]:
                        j=i+1
                        break
                    j+=1
                else:
                    return False
        return True"""
        i,j=0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)
        
