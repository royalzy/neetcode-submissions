class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join(c.lower() for c in s if c.isalnum() and ord(c) < 128)

        # start = ""
        # end = ""

        # for i in range(len(clean_text)//2):
        #     start = clean_text[i]
        #     end = clean_text[len(clean_text) - i -1]

        #     if start != end:
        #         return False

        # return True

        left, right = 0, len(clean_text) - 1
        while left < right:
            if clean_text[left] != clean_text[right]:
                return False
            left += 1
            right -= 1

        return True