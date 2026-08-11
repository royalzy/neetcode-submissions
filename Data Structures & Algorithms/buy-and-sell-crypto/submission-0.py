class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # left = 0
        # right = len(prices) - 1
        # selling_price = 0
        # buying_price = 0

        # while left < right:
        #     while prices[right] < prices[right - 1]:
        #         right -= 1
        #     while prices[left] > prices[left + 1]:
        #         left += 1
        #     selling_price = max(selling_price, prices[right])
        #     buying_price = min(buying_price, prices[left])
        #     if selling_price > buying_price:
        #         max_profit = max(max_profit, selling_price - buying_price)
        #         # issue is what if min and max is beyond

        # return max_profit

        max_profit = 0
        min_seen = prices[0]

        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - min_seen)
            min_seen = min(min_seen, prices[i])

        return max_profit

        


