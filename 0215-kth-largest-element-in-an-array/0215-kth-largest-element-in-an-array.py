class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums.copy()
        heapq.heapify(heap)
        
        for _ in range(len(nums) - k):
            heapq.heappop(heap)

        return heap[0]