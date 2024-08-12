class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0: return 1
            a = self.myPow(x, n//2)
            if n % 2: return a*a*x
            else: return a*a
        return helper(x, abs(n)) if n > 0 else 1/helper(x, abs(n))