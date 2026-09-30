class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l < r:
            m = l + (r - l) // 2
            row = matrix[m]

            if target < row[0]:
                r = m - 1
            elif target > row[-1]:
                l = m + 1
            else:
                l = m
                break

        row  = matrix[l]
        l, r = 0, len(row) - 1

        while l <= r:
            m = l + (r - l) // 2
            val = row[m]

            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return True

        return False