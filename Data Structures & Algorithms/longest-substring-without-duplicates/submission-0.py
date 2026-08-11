class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding
        # if s = "":
        #     return 0
        # left = 0
        # right = left + 1
        # cur_length = 0
        # max_length = 0
        # arr = [s[0]]

        # while right < len(s):
        #     if s[right] not in arr:
        #         right += 1
        #         arr.append(s[right])
        #         cur_length += 1
        #         max_length = max(max_length, cur_length)

        #     else:
        #         while arr.pop(0) != s[right]:
        #             cur_length -= 1





        # return max_length    


        left = 0
        char_set = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
        