class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer
        left = 0
        right = len(numbers) - 1

        while left < right:
            sumNums = numbers[left] + numbers[right]

            if sumNums == target:
                return [left+1, right+1]

            elif sumNums > target:
                right -= 1

            elif sumNums < target:
                left += 1
        
        return []

