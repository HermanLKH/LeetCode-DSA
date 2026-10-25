class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        if k == 0:
            return

        l, r = 0, k
        cnt = 0
        start = 0

        while cnt < len(nums):
            current = start
            temp = nums[current]

            while True:
                r = (current + k) % len(nums)

                temp2 = nums[r]
                nums[r] = temp
                temp = temp2

                current = r
                cnt += 1

                if current == start:
                    break
        
            start += 1