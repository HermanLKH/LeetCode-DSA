class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l < r:
            m = l + (r - l) // 2
            row = matrix[m]

            if row[0] < target:
                l = m + 1

                if row[-1] > target:
                    l = m
                    break
                elif row[-1] == target:
                    return True
            elif row[0] > target:
                r = m - 1
            else:
                return True
        
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