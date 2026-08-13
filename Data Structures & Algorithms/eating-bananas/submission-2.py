import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        worst = max(piles)
        if h <= len(piles):
            return worst

        l, r = 1, worst

        while l <= r:
            speed = l + (r-l) // 2
            hour_needed = 0

            for ban in piles:
                hour_needed += math.ceil(ban/speed)
                if hour_needed > h:
                    l = speed + 1
                    break

            if hour_needed <= h:
                worst = min(worst, speed)
                r = speed - 1
            
        return worst




