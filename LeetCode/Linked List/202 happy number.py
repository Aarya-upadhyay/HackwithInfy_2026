class Solution:
    def isHappy(self, n: int) -> bool:

        def func(num):
            s = 0
            while num:
                digit = num % 10
                s += digit * digit
                num //= 10
            return s

        slow = n
        fast = n

        while True:
            slow = func(slow)
            fast = func(func(fast))

            if slow == fast:
                break

        return slow == 1
