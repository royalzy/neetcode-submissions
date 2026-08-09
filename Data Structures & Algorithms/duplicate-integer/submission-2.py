class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_num = set(nums)
        return len(nums) > len(unique_num)