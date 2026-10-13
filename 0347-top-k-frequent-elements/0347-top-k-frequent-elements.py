# Time complexity:  O(N + k log M), M = number of unique numbers
# Space complexity: O(M + k)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        count = {}
        heap  = []

        # Time complexity: O(N)
        for num in nums:
            count[num] = count.get(num, 0) - 1

        # Time complexity: O(M), M = number of unique numbers
        for num, cnt in count.items():
            heap.append((cnt, num))

        # Time complexity: O(M)
        heapq.heapify(heap)

        # Time complexity: O(k log M)
        return [heapq.heappop(heap)[1] for _ in range(k)]
        
        # TOO EASY...
        # return heapq.nlargest(k, count.keys(), key=count.get)
