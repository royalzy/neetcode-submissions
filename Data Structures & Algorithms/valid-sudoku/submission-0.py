class Solution:
    def is_valid_group(self,group):
        seen = set()
        for char in group:
            if char != ".":
                if char in seen:
                    return False
                seen.add(char)
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force

        # row
        for row in board:
            if not self.is_valid_group(row):
                return False

        # column
        for col in range(9):
            column = [row[col] for row in board]
            if not self.is_valid_group(column):
                return False

        # 3x3 box
        for box in range(9):
            square = []
            for row in range(3):
                for col in range(3):
                    square.append(board[row+(box//3)*3][col+(3*(box%3))])

            if not self.is_valid_group(square):
                return False
        
        return True
