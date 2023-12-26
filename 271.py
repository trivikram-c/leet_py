## https://leetcode.com/problems/contains-duplicate/description/

## Beats 95.33 %

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        self_set = set()
        for num in nums:
            if num in self_set:
                return True
            else:
                self_set.add(num)
        
        return False

