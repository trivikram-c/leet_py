# https://leetcode.com/problems/valid-palindrome/description/

# Two pointer question
## Reduced branching can be a much better solve than lots of conditions but lower traversals
# 93% self

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n-1
        while i < j:
            while (s[i].isalnum() == False) and i < j:
                i += 1
                
            while (s[j].isalnum() == False) and j > i:
                j -=1
            
            if s[i].lower() != s[j].lower():
                return False
            else:
                j -= 1
                i += 1
        return True

#
## Another solution (faster and elegant)

## class Solution:
##     def isPalindrome(self, s: str) -> bool:
##         s = [i for i in s.lower() if i.isalnum()]
##         return s == s[::-1]
                
