# LeetCode 121 - Best Time to Buy and Sell Stock
# Runtime: 27ms - Beats 90.7%
# Status: Accepted - 212/212 test cases

class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
