class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        top, bot = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        '''
        thought process
        do binary search on last element of each row to get target row
        do binary search on target row
        '''
        while top <= bot:
            row = top + (bot - top) // 2
            if matrix[row][-1] == target:
                return True

            elif matrix[row][-1] < target:
                top = row + 1

            else:
                bot = row - 1


        while l <= r and top < len(matrix):
            mid = l + (r-l) //2
            if matrix[top][mid] == target:
                return True
            elif matrix[top][mid] < target:
                l = mid + 1

            else:
                r = mid - 1


        return False
