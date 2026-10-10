class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)

        cd = deque()
        time = 0

        while heap or cd:
            if not heap:
                time = cd[0][1]
            else:
                time += 1
                cnt = heapq.heappop(heap) + 1

                if cnt < 0:
                    cd.append([cnt, time + n])

            if cd and cd[0][1] == time:
                heapq.heappush(heap, cd.popleft()[0])

        return time
        