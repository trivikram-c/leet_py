# https://leetcode.com/problems/two-sum/submissions/1128690846/

# Beats 85% +

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, num in enumerate(nums):
            if num in mydict:
                return [i, mydict[num]]
            else:
                mydict[target-num] = i
