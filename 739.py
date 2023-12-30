# https://leetcode.com/problems/daily-temperatures/

# Idk, seems like a great approach

# Stacks which store both the pointer and the data

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = 0
        stack = []
        out = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            # if stack:
            while stack and stack[-1][0] < temp:
                curr_temp, curr_i = stack .pop()
                out[curr_i] = i - curr_i
                # days += 1
            stack.append([temp,i])
        return out
