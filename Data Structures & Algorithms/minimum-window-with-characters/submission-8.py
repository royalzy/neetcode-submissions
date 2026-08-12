from collections import Counter
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if len(t) == 0:
            return ""

        window = {}
        have = 0 
        countT = Counter(t)
        need = len(countT)
        res = [-1, -1]
        resLen = math.inf
        l = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        return s[res[0] : res[1] + 1] if resLen != math.inf else ""