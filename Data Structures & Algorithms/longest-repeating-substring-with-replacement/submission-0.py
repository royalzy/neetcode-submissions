class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # result = 0 
        # char = ""
        # rep = k

        # for left in range(len(s)):
        #     char = s[left]
        #     right = left
        #     while right < len(s):
        #         if s[right] != char:
        #             if rep > 0:
        #                 rep -= 1
        #             else:
        #                 rep = k
        #                 while s[left] == char:
        #                     left += 1
        #                 break
        #         right += 1
        #     result = max(result, right - left + 1)

        # return result

        result = 0
        chars = {}
        left = 0
        max_freq = 0

        for right in range(len(s)):
            chars[s[right]] = chars.get(s[right], 0) + 1
            max_freq = max(max_freq, chars[s[right]])

            while (right - left + 1) - max_freq > k:
                chars[s[left]] -= 1
                left += 1

            result = max(result, right-left+1)

        return result
