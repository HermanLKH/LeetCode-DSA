class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        prev_temps = []

        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]

            while prev_temps and temperatures[prev_temps[-1]] <= temp:
                prev_temps.pop()

            if prev_temps:
                res[i] = prev_temps[-1] - i
                
            prev_temps.append(i)

        return res
