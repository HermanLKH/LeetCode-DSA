# Time complexity:    O(N) => O(N log C), C <= 26
# Storage complexity: O(N)
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}

        # Time complexity: O(N), 
        for c in s:
            freq[c] = freq.get(c, 0) - 1

        # Time complexity: O(C) => O(C) + O(C), C <= 26
        heap = [(f, c) for c, f in freq.items()]
        heapq.heapify(heap)

        prev = None
        res  = []
        
        # Time complexity: O(1)
        if heap and -heap[0][0] > (len(s) + 1) // 2:
            return ""
        
        # Time complexity: O(N log C) => O(N log C) + O(N log C)
        while heap:
            # Time complexity: O(log C)
            f, c = heapq.heappop(heap)
            # Time complexity: O(1)
            res.append(c)

            # Time complexity: O(log C)
            if prev:
                heapq.heappush(heap, prev)

            f += 1
            prev = (f, c) if f < 0 else None

        # Time complexity: O(N)
        return "".join(res)
