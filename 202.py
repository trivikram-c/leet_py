class Solution:
    def isHappy(self, n: int) -> bool:
        stack = set([n])
        while True:
            out = 0
            while n:
                out += (n % 10)**2
                n = n // 10
            if out == 1: return True
            if out in stack: return False
            stack.add(out)
            n = out