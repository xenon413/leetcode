from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for k in range(i+1, len(prices)):
                if prices[i]>=prices[k]:
                    prices[i] -= prices[k]
                    break

        return prices
    