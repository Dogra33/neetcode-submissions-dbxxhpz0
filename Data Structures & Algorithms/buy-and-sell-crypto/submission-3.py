class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        left = 0
        right = left+1
        while left< right and right < len(prices):
            if prices[right] < min_price and right < len(prices)-1:
                min_price =  prices[right]
                left = right
                right = left+1

            profit = max(profit, (prices[right] - prices[left]))
            right +=1
        return profit