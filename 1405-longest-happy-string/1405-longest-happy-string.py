class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        prev = None
        res = []
        largest_cnt = min(-a, -b, -c)

        heap.append((-a, 'a')) if a > 0 else None
        heap.append((-b, 'b')) if b > 0 else None
        heap.append((-c, 'c')) if c > 0 else None

        heapq.heapify(heap)

        while heap:
            cnt, hc = heapq.heappop(heap)

            if cnt <= -2 and cnt <= largest_cnt:
                cnt += 2
                largest_cnt = cnt
                res.append(hc * 2)
            else:
                cnt += 1
                res.append(hc)

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if cnt < 0:
                prev = (cnt, hc)


        return "".join(res)