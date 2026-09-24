class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        l = 0
        max_length = 0
        highest_freq = 0

        for r in range(len(s)):
            char = s[r]
            counter[char] = counter.get(char, 0) + 1
            highest_freq = max(highest_freq, counter[char])
            while (r - l + 1) - highest_freq > k:
                counter[s[l]] -= 1
                l += 1
            max_length = max(r - l + 1, max_length)
        return max_length
