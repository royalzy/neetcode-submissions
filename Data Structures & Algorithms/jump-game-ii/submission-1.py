class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        chosen_max = 0
        current_max = 0
        min_jump = [0] * (len(nums) -1)
        jump = 0

        for i in range(len(nums)-1):
            jump_length = nums[i] + i 
            current_max = max(jump_length, current_max)
            if i >= chosen_max:
                chosen_max = current_max
                jump += 1
            min_jump[i] = jump
        print(min_jump)
        return min_jump[-1]

            