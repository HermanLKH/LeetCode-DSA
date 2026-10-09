class Solution:
    # Time complexity: O(n + (n - k) log n)
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Time complexity: O(n)
        heap = nums.copy()
        # Time complexity: O(n)
        heapq.heapify(heap)

        # Time complexity: O((n - k) log n)
        for _ in range(len(nums) - k):
            heapq.heappop(heap)

        # Time complexity: O(1)
        return heap[0]