class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        qTasks = deque(
            sorted(
                (qTime, pTime, i)
                for i, (qTime, pTime) in enumerate(tasks)
            )
        )

        heap  = []
        res   = [] 
        time  = 1

        while qTasks or heap:
            while qTasks:
                if qTasks[0][0] <= time:
                    qTime, pTime, i = qTasks.popleft()
                    heapq.heappush(heap, (pTime, i))
                else:
                    if not heap:
                        time = qTasks[0][0]
                    else:
                        break

            processing, i = heapq.heappop(heap)
            res.append(i)
            time += processing

        return res
