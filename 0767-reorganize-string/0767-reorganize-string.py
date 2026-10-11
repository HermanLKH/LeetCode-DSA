class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) - 1

        heap = [(f, c) for c, f in freq.items()]
        heapq.heapify(heap)

        prev = None
        res  = ""

        if heap and -heap[0][0] > (len(s) + 1) // 2:
            return ""
        
        while heap or prev:
            f, c = heapq.heappop(heap)
            res += c

            if prev:
                heapq.heappush(heap, prev)

            f += 1
            prev = (f, c) if f < 0 else None

        return res
