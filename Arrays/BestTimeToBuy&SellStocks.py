# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Logic: 1. 2 pointers l and r. If prices at l is greater then move l and r by 1 count
# 2. Profit is difference between right - left and maxprofit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l,r=0,1
        while r<len(prices):
            if prices[l]>prices[r]:
                l+=1
            profit = prices[r]-prices[l]
            maxP = max(maxP,profit)
            r+=1
        return maxP
