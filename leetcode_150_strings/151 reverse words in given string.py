class Solution:
    def reverseWords(self, s: str) -> str:
        """l=s.split()
        l.reverse()
        return " ".join(l)"""
        l=list(s)
        def reverse(le,ri):
            while le<ri:
                l[le],l[ri]=l[ri],l[le]
                le+=1
                ri-=1
        reverse(0,len(l)-1)
        i=0
        n=len(l)
        while i<n:
            if l[i]==" ":
                i+=1
                continue
            j=i
            while j<n and l[j]!=" ":
                j+=1
            reverse(i,j-1)
            i=j
        return " ".join(l)
