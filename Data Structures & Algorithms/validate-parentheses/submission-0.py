class Solution:
    def isValid(self, s: str) -> bool:
        # use stack

        stack = []
        valid = {'(':')', '{':'}','[':']'}

        for char in s:
            if char in valid.keys():
                stack.append(char)

            if char in valid.values():
                if stack == []:
                    return False
                if valid[stack[-1]] == char:
                    stack.pop()
                else: 
                    return False

        if stack == []:
            return True
        
        return False


        