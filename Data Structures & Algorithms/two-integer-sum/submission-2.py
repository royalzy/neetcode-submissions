class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            i_val = nums[i]
            if (target - i_val) in nums[i+1:]:
                return [i,nums.index((target - i_val),i+1)] 
        return False
        