class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = []
        total = 0

        for i in range(len(nums)):
            self.prefix.append((nums[i] + total, nums[i]))
            total = self.prefix[i][0]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right][0] - self.prefix[left][0] + self.prefix[left][1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)