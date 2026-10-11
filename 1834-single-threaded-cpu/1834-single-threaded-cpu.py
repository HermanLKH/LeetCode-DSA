class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        qHeap, pHeap = tasks.copy(), []

        for i, task in enumerate(qHeap):
            qHeap[i] = (task[0], task[1], i)

        heapq.heapify(qHeap)

        time = 1
        res  = []

        while qHeap or pHeap:
            while qHeap:
                if qHeap[0][0] <= time:
                    task = heapq.heappop(qHeap)
                    heapq.heappush(pHeap, (task[1], task[2]))

                else:
                    if not pHeap:
                        time = qHeap[0][0]
                    else:
                        break

            processed = heapq.heappop(pHeap)
            res.append(processed[1])

            time += processed[0]

        return res