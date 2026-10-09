class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums.copy()
        heapq.heapify(heap)
        res = 0
        
        for _ in range(len(nums) - k + 1):
            res = heapq.heappop(heap)

        return res