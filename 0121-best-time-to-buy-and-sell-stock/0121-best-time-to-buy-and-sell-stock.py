class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
        
        """
        max_profit = 0
        profits = []

        for i in range(len(prices) - 1):
            current_max = prices[i]
            for j in range(i + 1, len(prices)):
                if prices[j] > current_max:
                    current_max = prices[j]
            
            if current_max > prices[i]:
                profits.append(current_max - prices[i])

        if profits:
            return max(profits)
        else:
            return 0
        """
            
        