# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# 87%, copied, actual solution was very slow

# Somehow, calculating the sum everytime is faster than having the sum saved


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) -1
        while lo < hi:
            # sm = numbers[lo] + numbers[hi]
            if numbers[lo] + numbers[hi] < target:
                lo += 1
            elif numbers[lo] + numbers[hi] > target:
                hi -=1
            else:
                return [lo+1, hi+1]
        # for i, num in enumerate(numbers):
        #     if target - num in numbers[i+1:] :
        #         i2 = numbers[i+1:].index(target-num)
        #         return [i+1, i+1+ i2+1] 
