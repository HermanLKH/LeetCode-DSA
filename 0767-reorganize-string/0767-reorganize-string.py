class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        cd   = []
        heap = []
        res  = ""

        for c in s:
            freq[c] = freq.get(c, 0) - 1

        for c, f in freq.items():
            heap.append((f, c))

        heapq.heapify(heap)
        
        while heap or cd:
            f, c = heapq.heappop(heap)

            res += c

            while cd:
                heapq.heappush(heap, cd.pop())

            f += 1

            if f < 0:
                cd.append((f, c))

            if not heap and cd:
                return ''

        return res
