class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        total = 0
        window = deque()
        shortest = 0

        for num in nums:
            window.append(num)
            total += num

            while window and total - window[0] >= target:
                total -= window.popleft()

            if total >= target:
                if shortest == 0:
                    shortest = len(window)
                else:
                    shortest = min(shortest, len(window))

        return shortest
        