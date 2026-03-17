class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """s="".join(sorted(s))
        res=""
        for i in range(len(s)):
            if s[i] not in res:
                res+=s[i]
        return res"""
        l={c:i for i , c in enumerate(s)}
        visited=set()
        stk=[]
        for i,ch in enumerate(s):
            if ch not in visited:
                while stk and ch<stk[-1] and i<l[stk[-1]]:
                    visited.remove(stk.pop())
                stk.append(ch)
                visited.add(ch)
        return "".join(stk)
