class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        res = []

        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heap.append([dist, (point[0], point[1])])

        heapq.heapify(heap)

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res