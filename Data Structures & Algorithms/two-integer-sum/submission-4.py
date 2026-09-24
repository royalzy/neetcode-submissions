class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, value in enumerate(nums):
            needed = target - value
            if needed not in dic:
                dic[value] = i
            else:
                return [dic[needed], i]