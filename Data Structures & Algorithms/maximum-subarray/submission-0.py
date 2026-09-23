class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            subarray_sum = dp[i-1] + nums[i]
            if subarray_sum >= nums[i]:
                dp[i] = subarray_sum
            else:
                dp[i] = nums[i]

            res = max(res, dp[i])
        print(dp)
        return res



        
