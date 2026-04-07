class Solution:
    def isValid(self, s: str) -> bool:
        map={')':'(',
        '}':'{',
        ']':'['}
        stack=[]
        for ch in s:
            if ch in map:
                if not stack or stack[-1]!=map[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack
        
