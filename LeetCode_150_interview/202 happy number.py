class Solution:
    def isHappy(self, n: int) -> bool:
        """seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            s = 0
            while n:
                digit = n % 10
                s += digit * digit
                n //= 10

            n = s

        return True"""
        def getnext(num: int) -> int:
            summ = 0
            while num > 0:
                digit = num % 10
                summ += digit * digit 
                num = num // 10
            return summ

        slow = n 
        fast = n 

        while True:
            slow = getnext(slow)
            fast = getnext(getnext(fast))

            if fast == 1:
                return True
            if fast == slow:
                return False

