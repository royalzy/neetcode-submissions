class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while nums[l] > nums[r]:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid

        # rotated = l
        # if rotated != 0:
        #     sorted_nums = nums[rotated + 1: len(nums)] + nums[0: rotated]
        return nums[l]

        