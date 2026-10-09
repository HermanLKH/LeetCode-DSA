class Solution:
    # Time complexity: O(n log n)
    # if k is very close or equals to len of numbers, can just do sort
    # because k≈n, heap solution could cost O(n + n log n) which is not faster than sort
    # and this is more clean & concise
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]
