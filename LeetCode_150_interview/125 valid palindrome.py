class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==1 or len(s)==0:
            return True
        s=s.lower()
        strs=""
        """for i in s:
            if i.isalpha() or i.isdigit():
                strs+=i
            else:
                continue"""
        """strs1=strs[::-1]
        if strs==strs1:
            return True
        else:
            return False"""
        
        """if strs[0]!=strs[-1]:
            return False
        return isPalindrome(s[1:-1])"""

        """ return strs==strs[::-1]"""

        l=0
        r=len(s)-1
        while l<r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
