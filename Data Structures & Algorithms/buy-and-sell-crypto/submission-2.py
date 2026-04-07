class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        left = 0
        right = left+1
        while left< right and right < len(prices):
            print("Right price = ", prices[right])
            if prices[right] < min_price and right < len(prices)-1:
                min_price =  prices[right]
                left = right
                right = left+1
                print("Min = ", min_price)
            elif prices[right] < min_price and right == len(prices)-1:
                print("End elemnt")

            profit = max(profit, (prices[right] - prices[left]))
            print("--> ", profit)
            right +=1
        return profit