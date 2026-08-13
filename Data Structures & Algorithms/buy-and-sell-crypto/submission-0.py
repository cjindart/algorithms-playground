class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minVal = float("inf")

        for i in range(len(prices)):
            minVal = min(minVal, prices[i])
            if prices[i] - minVal > profit:
                profit = prices[i] - minVal
            
        return profit
