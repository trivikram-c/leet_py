# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1141934038/

# 93+ copied

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l,r = 0, len(prices)-1
        # minL, minL_i = prices[l], l
        # maxR maxR_i = prices[r], r
        # while l < r:
        #     if prices[l] < prices[r]:
        #         # if minL > prices[l]:
        #         #     minL, minL_i = prices[l], l
        #         minL = min(minL, prices[l])
        #         l += 1
        #     else :
        l,r = 0, 1
        max_profit = 0
        while r < len(prices):
            currentProf = prices[r] - prices[l]
            if prices[l] < prices[r]:
                max_profit = max(max_profit, currentProf)
            else:
                l = r  
            r += 1
    return max_profit