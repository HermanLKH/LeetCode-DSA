class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        boats_needed = 0
        l, r = 0, len(people) - 1

        people.sort()

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1

            r -= 1
            boats_needed += 1

        return boats_needed