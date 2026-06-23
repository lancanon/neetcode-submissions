from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows and columns
        ROWS, COLS = len(matrix), len(matrix[0])

        # Step 1: Binary search to find the correct row
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:  # Target is greater than the last item in row
                top = row + 1
            elif target < matrix[row][0]:  # Target is less than the first item in row
                bot = row - 1
            else:
                break  # Target must be within this row

        # No valid row found
        if not (top <= bot):
            return False

        # Use binary search on the found row
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True

        return False
