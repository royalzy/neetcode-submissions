class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        thought process

        1 pointer start left
        max_area = 0
        for i in range heights
            if min(all height before and at i) * i > max_area
                max_area = min(all height before and at i) * i

        can do two pointer? sliding window?
        calculate area for current height with r
        with l, slide until valid where valid means height onwards >= height at r
        '''
        '''
        solution from vid

        for col in heights (keep track of which index col is at)
            if col is bigger or equal than previous col
                append col to stack

            if col is smaller than previous col
                pop the bigger col until previous col is no longer smaller
                during this process
                for the col thats being popped , area of that col is (current col index - index of that col) * height of that col
                max_height = max(max_height,area)

        return max_height
        '''
        if not heights:
            return 0
        max_area = 0
        stack = []
        heights.append(0)

        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                area = h * w
                max_area = max(area, max_area)

            stack.append(i)


        return max_area
                
    



