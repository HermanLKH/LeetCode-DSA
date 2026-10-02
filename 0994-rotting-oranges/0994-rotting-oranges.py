class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        if len(q) < 1:
            return -1
        
        while q and fresh > 0:
            rot_count = len(q)

            for _ in range(rot_count):
                rotten = q.popleft()
                rot_i = rotten[0]
                rot_j = rotten[1]

                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    i, j = rot_i + di, rot_j + dj

                    if i < 0 or i >= rows or j < 0 or j >= cols:
                        continue
                    
                    if grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh -= 1
                        q.append((i, j))

            minutes += 1

        if fresh == 0:
            return minutes
        return -1