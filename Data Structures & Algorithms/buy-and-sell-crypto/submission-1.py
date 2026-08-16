class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minVal = float("inf")

        for price in prices:
            minVal = min(minVal, price)

            if price - minVal > profit:
                profit = price - minVal
        
        return profit