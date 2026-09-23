class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
        '(': ')',
        '{': '}',
        '[' :']',
        }
        stack = []
        for i in range(len(s)):
            if not stack or s[i] in dic:
                stack.append(s[i])
            else:
                corresponding = stack.pop()
                if corresponding not in dic or dic[corresponding] != s[i]:
                    return False

        return True if not stack else False
