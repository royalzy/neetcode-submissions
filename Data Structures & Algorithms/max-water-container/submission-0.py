class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer
        # You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

        # Find two lines that together with the x-axis form a container, such that the container contains the most water.

        # Return the maximum amount of water a container can store.

        # Notice that you may not slant the container.
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            water = min(heights[left], heights[right]) * (right - left)

            max_water = max(max_water, water)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_water
        