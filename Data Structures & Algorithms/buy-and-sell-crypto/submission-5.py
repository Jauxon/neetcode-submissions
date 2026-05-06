class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_so_far = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_so_far:
                min_so_far = prices[i]
                print(min_so_far)
            if prices[i] - min_so_far > max_profit:
                max_profit = prices[i] - min_so_far
                print(max_profit)
        return max_profit 