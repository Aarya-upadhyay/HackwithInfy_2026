class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # Sort children by greed
        s.sort()  # Sort cookies by size
        
        child_i = 0
        cookie_j = 0
        
        # While we still have children to feed AND cookies to give
        while child_i < len(g) and cookie_j < len(s):
            # If the current cookie can satisfy the current child
            if s[cookie_j] >= g[child_i]:
                child_i += 1  # This child is happy, move to next child
            
            # Regardless of if the child was fed, move to the next cookie
            cookie_j += 1
            
        return child_i # The number of happy children
