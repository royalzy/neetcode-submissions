class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(c.lower() for c in s if c.isalnum())

        l, r = 0, len(string) - 1
        
        while l < r:
            if string[l] != string[r]:
                return False
            r -= 1
            l += 1

        return True
