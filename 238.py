# https://leetcode.com/problems/product-of-array-except-self/description/

# 96% (solution seen, couldn't guess myself)


# Concept of traversing a list from the front and back

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        suffix = 1
        result = [1]*n
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        for i in range(n-1,-1,-1):
            result[i] *= suffix
            suffix *= nums[i]
        return result

