class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        count = {}

        for i, value in enumerate(numbers):
            needed = target - value
            if needed in count:
                return [count[needed] + 1, i + 1]

            count[value] = i

        return []