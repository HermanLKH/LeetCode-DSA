class Solution:
    # Time complexity: O(n + (n - k) log k)
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Time complexity: O(k)
        heap = nums[:k]
        # Time complexity: O(k)
        heapq.heapify(heap)

        # Time complexity: O(n - k + (n - k) log k)
        for n in nums[k:]:
            if n > heap[0]:
                heapq.heappushpop(heap, n)

        # Time complexity: O(1)
        return heap[0]