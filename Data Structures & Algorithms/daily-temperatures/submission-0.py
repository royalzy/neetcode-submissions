class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack

        stack = []
        result = [0] * len(temperatures)
        for day in range(len(temperatures)):
            while stack and temperatures[day] > temperatures[stack[-1]]:
                result[stack[-1]] = day - stack[-1]
                stack.pop()

            stack.append(day)
        
        return result
            


'''
thought process:

maintain a stack of day (indices)
look at today temp
if not greater than previous temp
add that to stack
while greater than previous temp
    previous temp output should be day - how many times popped to get to that day
if temp is still in stack, set output to 0
'''
