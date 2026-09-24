class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        max_length = 0
        length = 0
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                length -= 1
            
            seen.add(s[r])
            length += 1
            max_length = max(max_length, length)

        return max_length

                