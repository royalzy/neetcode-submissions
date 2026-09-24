class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_max = 0
        n = len(nums) - 1 # last index
        

        for i in range(len(nums)):
            if i > current_max:
                break
            max_jump_from_curr = nums[i] + i
            print(max_jump_from_curr)
            if max_jump_from_curr >= n:
                return True
            if max_jump_from_curr > current_max:
                current_max = max_jump_from_curr 

        return False