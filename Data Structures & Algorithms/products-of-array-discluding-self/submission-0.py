class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # divide and conquer
        total = [1] * len(nums)
        left = [1] * len(nums)
        left[0] = 1
        right = [1] * len(nums)
        right[-1] = 1

        for i in range(1,len(nums)):
            # left
            # so this will be prod of everything that comes before i
            left[i] = left[i-1] * nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            # right
            right[i] = right[i+1] * nums[i+1]

        # total
        # prod of left and right
        for i in range(len(nums)):
            total[i] = left[i] * right[i]

        return total
