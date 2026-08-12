import math
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        min_length = math.inf
        counter = Counter(t)
        left = 0
        res = ""

        for right in range(len(s)):
            # check if right of s is in counter
            if s[right] in counter:
                counter[s[right]] = counter[s[right]] - 1

            # get length of right - left + 1 and update min_length
            while (right - left + 1) >= len(t) and all(num <= 0 for num in counter.values()):
                if s[left] not in counter:
                    left += 1

                elif s[left] in counter and (counter[s[left]] + 1 <= 0):
                    counter[s[left]] = counter[s[left]] + 1
                    left += 1
                
                else:
                    if right - left + 1 < min_length:
                        min_length = right - left + 1
                        res = s[left:right + 1]

                    counter[s[left]] = counter[s[left]] + 1
                    left += 1


        return res

