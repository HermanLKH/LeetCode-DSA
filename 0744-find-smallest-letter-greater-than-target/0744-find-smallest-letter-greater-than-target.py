class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        l, r = 0, len(letters) - 1

        while l < r:
            m = l + (r - l) // 2

            letter = letters[m]

            if letter <= target:
                l = m + 1
            else:
                r = m
            
        if letters[l] <= target:
            return letters[0]
        else:
            return letters[l]


        