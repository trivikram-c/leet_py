# https://leetcode.com/problems/longest-consecutive-sequence/

# Beats 99.9 (seen). Tried a dictionary approach which also nearly as fast. Instead of set, use dict. I think it'll use more memory though.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # num_dict = defaultdict(lamda : False)
        num_set = set(nums)
        longest = 0
        for n in num_set:
            if n-1 not in num_set:
                length = 1
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest
