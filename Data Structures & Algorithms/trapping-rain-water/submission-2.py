class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0
        l, r = 0, len(height) - 1
        left_height, right_height = height[l], height[r]
        while l < r:
            if height[l] > height[r]:
                r -= 1
                right_height = max(right_height, height[r])
                trapped_water += right_height - height[r]

            elif height[r] >= height[l]:
                l += 1
                left_height = max(left_height, height[l])
                trapped_water += left_height - height[l]



        return trapped_water