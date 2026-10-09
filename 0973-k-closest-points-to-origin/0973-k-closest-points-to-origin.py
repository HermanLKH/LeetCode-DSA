class Solution:
    # Time complexity: O(n + k log n) => O(n)
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        res = []

        # Time complexity: O(n)
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heap.append((dist, point))

        # Time complexity: O(n)
        heapq.heapify(heap)

        # Time complexity: O(k log n)
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res