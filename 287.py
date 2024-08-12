class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow , fast = 0, 0
        # n = len(nums)
        # while True:
        #     if slow == fast:
        #         fast = (fast + 1)% n
        #     if nums[slow] == nums[fast] :
        #         return nums[slow]
        #     slow = (slow + 1)% n
        #     fast = (fast + 2)% n
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow  = nums[slow]
            if slow == slow2:
                break
        return slow