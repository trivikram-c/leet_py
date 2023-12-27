# https://leetcode.com/problems/3sum/description/

# Hashmap solution tried, but it didn't work
# 99% but copied
# Mulitple pointers approach

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        # class Solution:
    # def threeSum(self, nums):
        nums.sort()
        answer = []
        
        if len(nums) < 3:
            return answer
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            low, high = i + 1, len(nums) - 1
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                if s > 0:
                    high -= 1
                elif s < 0:
                    low += 1
                else:
                    answer.append([nums[i], nums[low], nums[high]])
                    lastLowOccurrence, lastHighOccurrence = nums[low], nums[high]
                    
                    while low < high and nums[low] == lastLowOccurrence:
                        low += 1
                    
                    while low < high and nums[high] == lastHighOccurrence:
                        high -= 1
        
        return answer
        # out = []
        # if len(nums) < 3:
        #     return out
        # nums = sorted(nums)
        # num_dict = {element:index for index, element in enumerate(nums)}
        # for i1, num1 in enumerate(nums[:-2]):
        #     target1 = -1*num1
        #     for i2, num2 in enumerate(nums[i1+1:-1]):
        #         target2 = target1 - num2
        #         if target2 in num_dict:
        #             if num_dict[target2] > i2 and num_dict[target1] > i1:
        #                 out.append([num1, num2, target2])
        # # out = list(set(out))
        # return out
                

    #     out = [[]]
    #     nums = sorted(nums)
    #     for i, num1 in enumerate(nums[:-2]):
    #         target = -1*num1
            
    #         if self.twoSum(target,nums[i+1:]) != False:
    #             out.append[]


    # def twoSum(self, target, lst):
    #     # tup = 
    #     lo = 0
    #     hi = len(lst)-1
    #     while lo < hi:
    #         if lst[lo] + lst[hi] < target:
    #             lo +=1
    #         elif lst[lo] + lst[hi] > target:
    #             hi -=1
    #         elif lst[lo] + lst[hi] == target:
    #             return [lst[lo],lst[hi]]
    # 
        # return False
        
