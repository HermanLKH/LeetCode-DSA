class NumArray:
    # Time complexity:  O(N)
    # Space complexity: O(N)
    def __init__(self, nums: list[int]):
        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    # Time complexity:  O(1)
    # Space complexity: O(1)
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)