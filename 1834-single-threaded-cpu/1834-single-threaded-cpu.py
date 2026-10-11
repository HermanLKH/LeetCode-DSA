# Time complexity:   O(N log N) => O(N log N) + O(N log N)
# Storage Complexiy: O(N)
class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        # Time complexity: O(N log N)
        qTasks = deque(
            sorted(
                (qTime, pTime, i)
                for i, (qTime, pTime) in enumerate(tasks)
            )
        )

        heap  = []
        res   = [] 
        time  = 1

        # Time complexity: O(N log N) => O(N log N) + O(N log N)
        while qTasks or heap:
            while qTasks:
                if qTasks[0][0] <= time:
                    # Time complexity: O(1)
                    qTime, pTime, i = qTasks.popleft()
                    # Time complexity: O(log N)
                    heapq.heappush(heap, (pTime, i))
                else:
                    if not heap:
                        time = qTasks[0][0]
                    else:
                        break

            # Time complexity: O(log N)
            processing, i = heapq.heappop(heap)
            res.append(i)
            time += processing

        return res
