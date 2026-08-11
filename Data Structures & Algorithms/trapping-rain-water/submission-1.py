class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer
        # if len(height) <= 2:
        #     return 0
        # trapped = 0
        # left = 0
        # right = 1
        # blocks = 0

        # while left < right and right < len(height):
        #     col_left = height[left]
        #     col_right = height[right]

        #     if col_right >= col_left:
        #         water_trapped = col_left  * (right - left - 1) - blocks
        #         # left is smaller than right
        #         trapped += water_trapped
        #         right += 1
        #         left = right - 1
        #         blocks = 0

        #     elif col_left > col_right:
        #         right += 1
        #         blocks += col_right

        # return trapped

        # if len(height) <= 2:
        #     return 0

        # trapped = 0
        # left = 0
        # right = len(height) - 1
        # max_left = 0
        # max_right = 0

        # while left < right:
        #     max_left = max(height[left], max_left)
        #     max_right = max(height[right], max_right)
        #     blocks = sum([(min(c,(min(max_left, max_right)))) if c >= (min(max_left, max_right)) else 0 for c in height[left:right]])

        #     water = max(min(max_left, max_right) - blocks,0)
        #     print(water)
        #     trapped += water
        #     if height[left] > height[right]:
        #         right -= 1
        #     else:
        #         left += 1

        # return trapped


        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        trapped = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    trapped += max_left - height[left]

                left += 1

            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    trapped += max_right - height[right]

                right -= 1

        return trapped

